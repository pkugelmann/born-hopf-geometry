#!/usr/bin/env python3
"""Replace the four versioned Born–Hopf snapshots and derive browser-friendly indices.

Provenance policy: ZIP members are copied byte-for-byte, root paper pairs are
checked against the current paper inventory; DAG data is presented as an
index, NOT an independent proof or source-action certificate.

Usage:
 python3 scripts/refresh_framework.py --papers PATH --audits PATH --dag PATH --geometry PATH
 python3 scripts/render_content.py
 python3 scripts/check_site.py
"""
import argparse,csv,hashlib,html,io,json,re,shutil,sys,zipfile
from pathlib import Path
import mistune
try:
    from pypdf import PdfReader
except ImportError:
    PdfReader=None

ROOT=Path(__file__).resolve().parents[1]; DOC=ROOT/'docs'
MAN=DOC/'manuscripts'; DATA=DOC/'data'
H=lambda x:html.escape(str(x),quote=True)
MD=mistune.create_markdown(escape=True,plugins=['table','strikethrough','url'])
LABELS={'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7}
VOL=['I','II','III','IV','V','VI','VII']

def filehash(b):return hashlib.sha256(b).hexdigest()
def safety(name):
    path=Path(name)
    if path.is_absolute() or '..' in path.parts or '\\' in name:raise ValueError('Unsafe ZIP entry '+name)
def openzip(path,rooted=False):
    z=zipfile.ZipFile(path)
    names=[x for x in z.namelist() if not x.endswith('/')]
    for n in names:safety(n)
    prefix=names[0].split('/')[0]+'/' if rooted else ''
    if rooted and any(not n.startswith(prefix) for n in names):raise ValueError('Unexpected ZIP roots')
    return z,prefix

def clearfiles(dir):
    if dir.exists():shutil.rmtree(dir)
    dir.mkdir(parents=True)

def read_json(z,n):return json.loads(z.read(n))
def write_json(path,obj):path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def pretty(version):return version.replace('_','.')

def report_page(title,body,download_path):
    # Paths are relative to site root via <base>, retaining the same template.
    base=(DOC/'verification/reports/Paper1A-ProofChainAudit-v1_9.html')
    old=base.read_text(encoding='utf-8') if base.exists() else (DOC/'index.html').read_text(encoding='utf-8')
    head=old.split('<main id="main">',1)[0]
    if '<base href="../../">' not in head:head=head.replace('<head>','<head><base href="../../">',1)
    head=re.sub(r'<title>.*?</title>',f'<title>{H(title)} · Born–Hopf Geometry</title>',head)
    foot=old.split('</main>',1)[1]
    main=(f'<section class="page-hero"><div class="container"><div class="eyebrow"><a class="micro-link" href="verification.html">← Verification</a> · Original audit record</div>'
          f'<h1 style="font-size:clamp(2rem,3.4vw,3.25rem)">{H(title)}</h1><p>Historical source and audit scope are preserved. This rendering does not upgrade the underlying proof status.</p>'
          f'<a class="btn btn-secondary" download href="{H(download_path)}">Original Markdown ↓</a></div></section>'
          f'<div class="container page-section"><div class="notice"><strong>Source version matters.</strong> Paper text may be newer than this audit. Do not infer a current E3/E4 result from a historical verdict.</div>'
          f'<article class="prose report-prose">{body}</article></div>')
    # Mistune interprets [G_u,G_v](x) in mathematical audit notation as a link.
    # Keep the underlying textual expression instead of emitting a broken href.
    main=main.replace('<a href="x">G_u,G_v</a>','[G_u,G_v](x)')
    return head+'<main id="main">'+main+'</main>'+foot

def main(args):
    pack={x:Path(getattr(args,x)).resolve() for x in ('papers','audits','dag','geometry')}
    for key,path in pack.items():
        if not path.exists():raise FileNotFoundError(f'{key}: {path}')
    paperver=re.search(r'v(\d+_\d+)',pack['papers'].name).group(1)
    auditver=re.search(r'v(\d+_\d+)',pack['audits'].name).group(1)
    dagver=re.search(r'v(\d+_\d+)',pack['dag'].name).group(1)
    geover=re.search(r'v(\d+_\d+)',pack['geometry'].name).group(1)
    # Validate cross-archive content and current source identities BEFORE touching the site.
    pz,pp=openzip(pack['papers']);az,ap=openzip(pack['audits'],True);dz,dp=openzip(pack['dag'],True);gz,gp=openzip(pack['geometry'],True)
    with pz,az,dz,gz:
        pn=[n for n in pz.namelist() if not n.endswith('/')]
        im=[n for n in pn if re.fullmatch(r'Paper00-PaperInventory-v\d+_\d+\.csv',n)]
        if len(im)!=1:raise ValueError('Need exactly one paper inventory')
        inv=list(csv.DictReader(io.StringIO(pz.read(im[0]).decode('utf-8-sig'))))
        if len(inv)!=31 or len(set(r.get('paper',r.get('code')) for r in inv))!=31:raise ValueError('Not 31 unique active paper roots')
        source_hash=filehash(pack['papers'].read_bytes());audit_hash=filehash(pack['audits'].read_bytes())
        active=read_json(dz,dp+f'DAG/ActiveRelease-v{dagver}.json')
        if active.get('source_archive_sha256')!=source_hash:raise ValueError('DAG points to different PapersMinimal source')
        if active.get('audit_archive_sha256')!=audit_hash:raise ValueError('DAG points to different audit release')
        ar=read_json(dz,dp+f'DAG/CurrentSourceAnchorMap-v{paperver}.json')
        assert len(ar['claims'])==active['current_source_label_count'],'Label census does not match atlas'
        if ar['duplicates']:raise ValueError('Duplicate source labels')
        issues=read_json(az,ap+'Paper00-RemainingProofObligations-v1_3.json')
        delta=read_json(pz,f'Paper00-SourceAnchorDelta-v{paperver}.json')
        if len(delta['records'])!=delta['new_label_count']:raise ValueError('Delta count error')
        for r in inv:
            for name,key in [(r['source'],r.get('tex_sha256',r.get('source_sha256'))),(r['pdf'],r['pdf_sha256'])]:
                if name not in pn or filehash(pz.read(name))!=key:raise ValueError('Paper inventory digest mismatch: '+name)
        # Replace only the site-managed scientific corpora, not edit-able prose.
        clearfiles(MAN)
        for n in pn:
            if '/' in n:continue # build/ and xref/ reside inside the full original ZIP
            dst=MAN/n;dst.write_bytes(pz.read(n))
        original=(DOC/'data/manifest.json')
        manifest=json.loads(original.read_text(encoding='utf-8'))
        prior={p['code']:p for p in manifest['papers']}
        newpapers=[]
        for r in inv:
            code=r.get('paper',r.get('code'))
            old=prior[code]
            pdf=r['pdf']; src=r['source']
            pages=len(PdfReader(io.BytesIO(pz.read(pdf))).pages) if PdfReader else int(old['pages'])
            p={**old,'source':'manuscripts/'+src,'pdf':'manuscripts/'+pdf,
               'sourceSha256':r.get('tex_sha256',r.get('source_sha256')),
               'pdfSha256':r['pdf_sha256'],'pages':pages,
               'pdfVersion':re.search(r'-v(\d+_\d+)\.pdf',pdf).group(1).replace('_','.'),
               'rebuildStatus':'See current release notes: individual PDFs have different rebuild status.'}
            newpapers.append(p)
        clearfiles(DOC/'verification/reports')
        clearfiles(DOC/'verification/registries')
        rawlist=[n[len(ap):] for n in az.namelist() if n.startswith(ap) and not n.endswith('/')]
        auditlist=[]; paper_audits={}
        for rel in sorted(rawlist):
            raw=az.read(ap+rel)
            if rel.endswith('.md'):
                (DOC/'verification/reports'/rel).write_bytes(raw)
                htmlpath='verification/reports/'+rel[:-3]+'.html'
                hpage=report_page(rel[:-3].replace('-',' '),MD(raw.decode('utf-8-sig')), 'verification/reports/'+rel)
                (DOC/htmlpath).write_text(hpage,encoding='utf-8')
                code=re.match(r'(Paper[1-7][A-G])-(?:ExceptionalGeometry)?ProofChainAudit-v',rel)
                if code:
                    paper_audits[code.group(1)]=htmlpath
                auditlist.append({'name':rel,'paper':code.group(1) if code else 'Cross-paper','href':htmlpath})
            elif rel.endswith('.json'):
                (DOC/'verification/registries'/rel).write_bytes(raw)
        for p in newpapers:p['audit']=paper_audits.get(p['code'])
        # Protocols live in content/protocols so future updates also work from a
        # normal GitHub clone; no reliance on a special /mnt/data mount.
        clearfiles(DOC/'verification/protocols')
        for f in sorted((ROOT/'content/protocols').glob('*.md')):
            (DOC/'verification/protocols'/f.name).write_bytes(f.read_bytes())
            page=report_page(f.stem.replace('-',' '),MD(f.read_text(encoding='utf-8')),
                             'verification/protocols/'+f.name)
            (DOC/'verification/protocols'/(f.stem+'.html')).write_text(page,encoding='utf-8')
        # Network diagrams: exact current SVG filenames and SHA; no fabricated diagrams.
        clearfiles(DOC/'geometry')
        diagrams=[]
        for n in sorted(gz.namelist()):
            if n.endswith('.svg'):
                rel=n[len(gp):].split('/')[-1]
                svg=gz.read(n)
                (DOC/'geometry'/rel).write_bytes(svg)
                diagrams.append({'file':rel,'name':rel.replace('.svg','').replace('_',' ').replace('batch','Batch '),
                                 'sha256':filehash(svg)})
        (DOC/'geometry'/f'Paper00-S3StructureNetwork-README-v{geover}.md').write_bytes(gz.read(gp+'README.md'))
        # Archived full original bundles, all now <100MiB per file.
        clearfiles(DATA)
        archives=[]
        for key,ver,label in [('papers',paperver,'PapersMinimal'),('audits',auditver,'ProofChainAudits'),('dag',dagver,'DAGAtlas'),('geometry',geover,'S3StructureNetwork')]:
            name=f'Paper00-{label}-v{ver}.zip';target=DATA/name;shutil.copyfile(pack[key],target)
            archives.append({'name':name,'version':label+' '+pretty('v'+ver),'bytes':target.stat().st_size,
                             'sha256':filehash(target.read_bytes()),'sitePath':'data/'+name,'publishing':'Downloadable on this site'})
        # NOTE: Atlas canonical node graph is inherited; current source anchors may be newer.
        canon=read_json(dz,dp+'DAG/Paper00-TheoremDAG.json')
        nodetitles={n.get('id'):n.get('title','') for n in canon['nodes'] if n.get('id')}
        latest={x['label']:x for x in delta['records']}
        refs={}
        for label,obj in ar['claims'].items():
            l=latest.get(label)
            title=nodetitles.get(label,'')
            if not title and l:
                title=re.search(r'\[(.*?)\]',l.get('source_context',''))
                title=title.group(1) if title else ''
            refs[label]={'id':label,'paper':obj['paper'],'line':obj['line'],
                         'file':obj['source_file'],'title':title,'new':bool(l)}
        nodes=[]
        for n in canon['nodes']:
            nid=n.get('id')
            if not nid:continue
            curr=ar['claims'].get(nid)
            nodes.append({'id':nid,'title':n.get('title',''), 'paper':n.get('paper',''),
                          'type':n.get('type',''), 'source_line':curr.get('line') if curr else None,
                          'current_anchor':bool(curr),'source_file':curr.get('source_file') if curr else ''})
        obligations=[]
        for x in issues['obligations']:
            obligations.append({'id':x.get('issue_id',''),'paper':x.get('paper',''),
                                'status':x.get('effective_status',''),
                                'description':x.get('original_exact_obligation') or x.get('retained_owner') or 'See original source registry',
                                'recorded_source':x.get('current_source','')})
        small={'sourceRelease':'v'+paperver,'dagRelease':'v'+dagver,'auditsRelease':'v'+auditver,
               'counts':{'papers':len(newpapers),'anchors':len(refs),'canonicalNodes':len(nodes),'obligations':len(obligations),'reports':len(auditlist),'diagrams':len(diagrams),'newLabels':len(latest)},
               'labels':list(refs.values()),'nodes':nodes,'obligations':obligations,'audits':auditlist,'diagrams':diagrams}
        (DOC/'assets/explorer-data.js').write_text('/* Generated from current source/audit indices; NOT a proof certificate */\nwindow.BH_EXPLORER='+json.dumps(small,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
        manifest.update(site='Paper00-GitHubPage-v1_2',snapshotDate='2026-11-20',papersRelease='v'+paperver,
                        auditRelease='v'+auditver,dagRelease='v'+dagver,geometryRelease='v'+geover,
                        papers=newpapers,archives=archives,audits=auditlist,diagrams=[x['file'] for x in diagrams],
                        statusNote='Source-integrated 55 new labels in v3.077; independent global E3/E4 and physical occurrence not promoted. The v1.83 audit obligations are historical source-versioned records.',
                        explorerCounts=small['counts'],
                        atlasStatus={'nodes':active['canonical_node_count'], 'proofEdges':active['canonical_proof_edges'],
                                     'strictEdges':active['canonical_strict_edges'],'sourceLabels':active['current_source_label_count'],
                                     'newLabelCount':active['new_source_labels_this_release'],
                                     'newProofEdges':active['new_material_proof_edges_this_release'],
                                     'proofPromotions':active['proof_status_promotions_this_release'],
                                     'occurrencePromotions':active['physical_occurrence_promotions']},
                        sourceReleaseSha256=source_hash)
        write_json(DATA/'manifest.json',manifest)
        cat=DOC/'assets/catalog.js';txt=cat.read_text(encoding='utf-8');key='window.BH_CATALOG=';oldcat=json.loads(txt[txt.index(key)+len(key):].strip().rstrip(';'))
        oldcat.update(papers=newpapers,release=pretty('v'+paperver),archives=archives)
        cat.write_text('/* Current paper inventory, verified SHA-256 */\nwindow.BH_CATALOG='+json.dumps(oldcat,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
        # Replace stale old-version strings in non-prose legacy pages.
        for rel in ('docs/papers.html','docs/downloads.html','docs/about.html','docs/verification.html','docs/geometry.html'):
            path=ROOT/rel
            s=path.read_text(encoding='utf-8')
            for old,new in [('v3.058',pretty('v'+paperver)),('v3_058','v'+paperver),('v1.79',pretty('v'+auditver)),('v1_79','v'+auditver),
                            ('v1.215',pretty('v'+dagver)),('v1_215','v'+dagver),('v1.41',pretty('v'+geover)),('v1_41','v'+geover)]:s=s.replace(old,new)
            path.write_text(s,encoding='utf-8')
        # Rebuild old inventory of report cards from up-to-date source, if page exists.
        verified=ROOT/'docs/verification.html'
        s=verified.read_text(encoding='utf-8')
        cards=''.join(f'<div class="audit-card"><span class="paper-code">{H(p["label"])}</span><strong>{H(p["title"])}</strong><p>{H(Path(p["audit"]).name)}</p><a href="{H(p["audit"])}">Read audit record ↗</a></div>' for p in newpapers if p.get('audit'))
        s=re.sub(r'<div class="audit-list">.*?</div>\s*</section>', '<div class="audit-list">'+cards+'</div></section>',s,count=1,flags=re.S)
        # Explicitly qualify older audit issue statistics (they are not current status counts).
        s=re.sub(r'<div class="notice"><strong>Status is scoped, not binary.</strong>.*?</div>',
                '<div class="notice"><strong>Versioned evidence, not blanket certification.</strong> The v1.83 audit archive preserves 31 paper-level reports and 130 historical pending-obligation rows. Some reports inspect older TeX versions. The v1.223 DAG overlays current v3.077 source anchors but freezes its canonical proof graph; the 55 newly integrated labels have no new global E3/E4 certification. <a href="research.html?type=obligations">Browse obligations →</a></div>',s,count=1,flags=re.S)
        verified.write_text(s,encoding='utf-8')
    print('Updated: 31 papers,',len(refs),'labels,',len(nodes),'canonical nodes,',len(obligations),'audited obligations,',len(auditlist),'reports,',len(diagrams),'diagrams.')
    print('Snapshots v'+paperver,'v'+auditver,'v'+dagver,'v'+geover)

if __name__=='__main__':
 p=argparse.ArgumentParser()
 for n in ('papers','audits','dag','geometry'):p.add_argument('--'+n,required=True)
 main(p.parse_args())
