#!/usr/bin/env python3
"""Publication integrity check: full current paper corpus, archive provenance,
search index, audit link targets, source anchors and local HTML links.

A PASS is a source/integrity/presentation check, never a proof audit.
"""
import hashlib,html.parser,json,pathlib,re,sys,zipfile
from urllib.parse import urlsplit, unquote
ROOT=pathlib.Path(__file__).resolve().parents[1];DOC=ROOT/'docs'; errors=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

class HTML(html.parser.HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.ids=set()
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if 'id' in d:self.ids.add(d['id'])
        if tag in ('a','link','script','img','iframe','source','base'):
            val=d.get('href') or d.get('src')
            if val:self.links.append((tag,val))

def bad(message):errors.append(message)
def need(ok,msg):
    if not ok:bad(msg)

m=json.loads((DOC/'data/manifest.json').read_text(encoding='utf-8'))
need(m['site']=='Paper00-GitHubPage-v1_4','Unexpected website package marker')
need(len(m['papers'])==31 and len({p['code'] for p in m['papers']})==31,'Not 31 distinct primary papers')
need(len(m['audits'])==45,'Not 45 Markdown audit reports')
need(len(m['diagrams'])==13,'Not 13 SVG diagrams')

pdf_seen=set();tex_seen=set()
for p in m['papers']:
    for kind,hashname,seen in [('pdf','pdfSha256',pdf_seen),('source','sourceSha256',tex_seen)]:
        path=DOC/p[kind]
        need(path.exists(),f'Missing {kind}: {path}')
        if path.exists():need(sha(path)==p[hashname],f'Digest mismatch {path}')
        need(path.name not in seen,f'Duplicate {kind} filename {path.name}')
        seen.add(path.name)
    need(bool(p.get('audit')) and (DOC/p['audit']).is_file(),p['code']+' audit link absent')
need(len(list((DOC/'manuscripts').glob('Paper*.pdf')))==31,'Unexpected superseded/absent paper PDFs')
need(len([p for p in (DOC/'manuscripts').glob('Paper*.tex') if re.match(r'Paper[1-7][A-G]-',p.name)])==31,'Unexpected superseded/absent primary paper TeX')

for a in m['archives']:
    f=DOC/a['sitePath']
    need(f.is_file(),f'Archive missing: {a["name"]}')
    if f.exists():
        need(f.stat().st_size==a['bytes'],f'Archive size mismatch: {a["name"]}')
        need(sha(f)==a['sha256'],f'Archive SHA-256 mismatch: {a["name"]}')
        need(f.stat().st_size<100*1024*1024,f'Archive exceeds GitHub single-file limit: {a["name"]}')

for visual in m.get('newVisuals',[]):
    p=DOC/visual['path']
    need(p.is_file(),f'Missing authored visual: {visual["path"]}')
    if p.is_file(): need(sha(p)==visual['sha256'],f'Visual digest mismatch: {p}')

for a in m['audits']:
    need((DOC/a['href']).is_file(),'Missing report page '+a['href'])
    need((DOC/'verification/reports'/a['name']).is_file(),'Missing original audit '+a['name'])
for g in m['diagrams']:
    need((DOC/'geometry'/g).is_file(),'Missing geometry diagram '+g)

s=(DOC/'assets/explorer-data.js').read_text(encoding='utf-8')
prefix='window.BH_EXPLORER='
try:browser=json.loads(s.split(prefix,1)[1].strip().rstrip(';'))
except Exception as e:bad(f'Explorer data invalid: {e}');browser={}
if browser:
    counts=browser['counts']
    for field,items in [('anchors','labels'),('canonicalNodes','nodes'),('obligations','obligations'),('reports','audits'),('diagrams','diagrams')]:
        need(len(browser[items])==counts[field],f'Explorer {field} count mismatch')
    need(len({x['id'] for x in browser['labels']})==14366,'Duplicated or missing current labels')
    need(sum(x['new'] for x in browser['labels'])==55,'Latest additions !=55')
    need(len({x['id'] for x in browser['nodes']})==7667,'Duplicate or missing inherited DAG nodes')
    need(counts['obligations']==130,'Retained obligation count changed')
    source_lines={}
    for x in browser['labels']:
        filename=x['file']
        if filename not in source_lines:
            f=DOC/'manuscripts'/filename
            if not f.exists():bad('Missing label source '+filename);continue
            source_lines[filename]=f.read_text(encoding='utf-8').splitlines()
        lines=source_lines[filename];n=x['line']
        if not (isinstance(n,int) and 0<n<=len(lines) and x['id'] in lines[n-1]):
            bad(f'Invalid exact source anchor {x["id"]}: {filename}:{n}')

# Check that the release's active DAG actually identifies the precise papers and audit bytes.
try:
    dag_path=next(DOC/'data'/a['name'] for a in m['archives'] if 'DAGAtlas' in a['name'])
    with zipfile.ZipFile(dag_path) as z:
        name=f'Paper00-DAGAtlas-{m["dagRelease"]}/DAG/ActiveRelease-{m["dagRelease"]}.json'
        active=json.loads(z.read(name))
    papers=next(a for a in m['archives'] if 'PapersMinimal' in a['name'])
    audits=next(a for a in m['archives'] if 'ProofChainAudits' in a['name'])
    need(active['source_archive_sha256']==papers['sha256'],'DAG/source ZIP SHA mismatch')
    need(active['audit_archive_sha256']==audits['sha256'],'DAG/audit ZIP SHA mismatch')
    need(active['current_source_label_count']==14366,'DAG current anchor count mismatch')
    need(active['canonical_node_count']==7667,'DAG canonical node count mismatch')
    need(active['proof_status_promotions_this_release']==0,'Unexpected proof-status promotion')
    need(active['physical_occurrence_promotions']==0,'Unexpected physical status promotion')
except Exception as ex:bad('Cannot check current DAG release metadata: '+str(ex))

files=list(DOC.rglob('*.html')); parsed={}
for f in files:
    obj=HTML();obj.feed(f.read_text(encoding='utf-8'))
    parsed[f.resolve()]=obj
for f,obj in parsed.items():
    base=f.parent
    for tag,link in obj.links:
        if tag=='base':
            base=(f.parent/link).resolve()
            continue
        if link.startswith(('http:','https:','mailto:','tel:','javascript:','data:')):continue
        parts=urlsplit(link);path=unquote(parts.path)
        dest=(base/path).resolve() if path else f
        if not dest.exists():bad(f'{f.relative_to(ROOT)}: broken link {link}')
        elif DOC.resolve() not in dest.parents and dest!=DOC.resolve():bad(f'{f.relative_to(ROOT)}: link escapes site {link}')
        # Check a local fragment only for public navigation pages. Audit reports
        # contain original Markdown citation syntax with historical fragment refs.
        elif parts.fragment and dest.suffix=='.html' and (f.parent==DOC):
            if dest in parsed and unquote(parts.fragment) not in parsed[dest].ids:
                bad(f'{f.relative_to(ROOT)}: broken anchor {link}')

for name in ['index.html','ideas.html','matter.html','papers.html','paper.html','framework.html','observables.html','pathways.html','updates.html','research.html','geometry.html','verification.html','downloads.html','about.html','glossary.html','.nojekyll']:
    need((DOC/name).exists(),'Missing publication entry '+name)
need((ROOT/'.github/workflows/pages.yml').exists(),'GitHub Pages workflow absent')
print(f"Checked {len(m['papers'])} current paper pairs, {len(m['audits'])} reports, {len(files)} HTML pages, {len(m['diagrams'])} SVGs, {len(browser.get('labels',[]))} exact label anchors and {len(m['archives'])} archive digests")
if errors:
    for e in errors[:100]:print('FAIL:',e)
    print('TOTAL:',len(errors),'integrity/navigation failures');sys.exit(1)
print('PASS: source hashes, cross-archive provenance, current source anchors and local links. This is NOT a global E3/E4 proof audit.')
