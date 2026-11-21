#!/usr/bin/env python3
"""Replace the manuscript corpus from one versioned PapersMinimal ZIP.

Usage: python3 scripts/refresh_manuscripts.py /path/to/Paper00-PapersMinimal-v3_058.zip

The helper never touches editorial content/ Markdown, audits or geometry diagrams.
It verifies input SHA-256 against the archive inventory before mutation.
After running, review explanatory claims and execute render_content.py.
"""
import csv, io, hashlib, json, pathlib, re, sys, zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOC = ROOT/'docs'
MAN = DOC/'manuscripts'

def digest_bytes(b): return hashlib.sha256(b).hexdigest()

def main(archive):
    m = re.fullmatch(r'Paper00-PapersMinimal-v(\d+)_(\d+)(?:\(\d+\))?\.zip', archive.name)
    if not m: raise ValueError('Expected a versioned Paper00-PapersMinimal-vU_W.zip file')
    version=f'v{m.group(1)}_{m.group(2)}'; pretty=f'v{m.group(1)}.{int(m.group(2)):03d}'
    with zipfile.ZipFile(archive) as z:
        names=[x for x in z.namelist() if not x.endswith('/')]
        if any(pathlib.PurePosixPath(x).is_absolute() or '..' in pathlib.PurePosixPath(x).parts for x in names):
            raise ValueError('Unsafe archive paths')
        matches=[x for x in names if re.fullmatch(r'Paper00-PaperInventory-v\d+_\d+\.csv',x)]
        if len(matches)!=1: raise ValueError('Archive inventory absent/ambiguous')
        rows=list(csv.DictReader(io.StringIO(z.read(matches[0]).decode('utf-8-sig'))))
        if len(rows)!=31: raise ValueError(f'Expected 31 manuscripts, got {len(rows)}')
        if len({r['code'] for r in rows})!=31: raise ValueError('Duplicate manuscript IDs')
        for r in rows:
            for kind,key in [('source','source_sha256'),('pdf','pdf_sha256')]:
                if r[kind] not in names or digest_bytes(z.read(r[kind]))!=r[key]:
                    raise ValueError(f'{r["code"]} {kind} does not match inventory')
        manifest=json.loads((DOC/'data/manifest.json').read_text(encoding='utf-8'))
        previous_version=manifest['papersRelease']
        previous_pretty=previous_version.replace('_','.')
        catalog=(DOC/'assets/catalog.js').read_text(encoding='utf-8')
        catalog_data=json.loads(catalog[catalog.index('window.BH_CATALOG=')+len('window.BH_CATALOG='):].strip().rstrip(';'))
        previous={p['code']:p for p in manifest['papers']}
        if set(previous)!={r['code'] for r in rows}: raise ValueError('Paper code mismatch')
        for p in MAN.rglob('*'):
            if p.is_file():p.unlink()
        for n in names:
            out=MAN/n
            out.parent.mkdir(exist_ok=True,parents=True)
            out.write_bytes(z.read(n))
    updated=[]
    for r in rows:
        p=previous[r['code']]
        p.update(source='manuscripts/'+r['source'],pdf='manuscripts/'+r['pdf'],
                 pages=int(r['pages']),sourceSha256=r['source_sha256'],pdfSha256=r['pdf_sha256'],
                 pdfVersion=re.search(r'-v([0-9_]+)\.pdf$',r['pdf']).group(1).replace('_','.'),
                 rebuildStatus=r['crossref_status'])
        updated.append(p)
    manifest['papers']=updated
    manifest['papersRelease']=version
    manifest['statusNote']='Paper corpus '+pretty+'; source-specific theorem scopes, open bridges and independent verification status remain governed by the versioned paper release notes and audits. No physical endpoint is promoted by replacing the archive.'
    for a in manifest['archives']:
        if 'PapersMinimal-' in a['name']:
            a.update(name=f'Paper00-PapersMinimal-{version}.zip', version='PapersMinimal '+pretty,
                     bytes=archive.stat().st_size,sha256=hashlib.file_digest(open(archive,'rb'),'sha256').hexdigest())
    (DOC/'data/manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    catalog_data['papers']=updated
    catalog_data['release']=pretty
    catalog_data['archives']=manifest['archives']
    (DOC/'assets/catalog.js').write_text('/* Auto-generated from the versioned PapersMinimal inventory. */\nwindow.BH_CATALOG='+json.dumps(catalog_data,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
    for relative in ('docs/papers.html','docs/downloads.html','docs/about.html','docs/verification.html','docs/assets/main.js'):
        file=ROOT/relative
        txt=file.read_text(encoding='utf-8')
        txt=txt.replace(previous_version,version).replace(previous_pretty,pretty)
        file.write_text(txt,encoding='utf-8')
    print('Refreshed',len(updated),'manuscripts to',version,'with exact inventory hashes.')
    print('Next: review content/*.md and run python scripts/render_content.py then python scripts/check_site.py')

if __name__=='__main__':
    if len(sys.argv)!=2:raise SystemExit('Usage: python scripts/refresh_manuscripts.py <PapersMinimal ZIP>')
    main(pathlib.Path(sys.argv[1]).resolve())
