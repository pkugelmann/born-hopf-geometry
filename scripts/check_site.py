#!/usr/bin/env python3
"""Dependency-free local integrity checks for the shipped static website."""
import json, pathlib, hashlib, re, sys, html.parser
ROOT=pathlib.Path(__file__).resolve().parents[1]
DOC=ROOT/'docs'
class Links(html.parser.HTMLParser):
 def __init__(self):super().__init__();self.links=[]
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if tag in ('a','link','script','img','base'):
   val=d.get('href') or d.get('src')
   if val:self.links.append((tag,val))
errors=[]
manifest=json.loads((DOC/'data/manifest.json').read_text())
if len(manifest['papers'])!=31:errors.append('Expected 31 papers')
for p in manifest['papers']:
 for kind in ('source','pdf'):
  target=DOC/p[kind]
  if not target.is_file():errors.append('Missing '+str(target))
  else:
   digest=hashlib.sha256(target.read_bytes()).hexdigest()
   expected=p['sourceSha256'] if kind=='source' else p['pdfSha256']
   if digest!=expected:errors.append('Hash mismatch '+str(target))
for f in DOC.rglob('*.html'):
 l=Links();l.feed(f.read_text(encoding='utf-8'))
 base=f.parent
 for tag,link in l.links:
  if tag=='base':
   base=(f.parent/link).resolve()
   continue
  if link.startswith(('#','https:','http:','mailto:','tel:','javascript:','data:')):continue
  path=link.split('#')[0].split('?')[0]
  if not path:continue
  dest=(base/path).resolve()
  if not dest.exists():errors.append(f'{f.relative_to(ROOT)}: broken {link}')
  elif DOC not in dest.parents and dest!=DOC:errors.append(f'{f.relative_to(ROOT)}: escaped site root {link}')
for x in ['index.html','papers.html','framework.html','geometry.html','verification.html','downloads.html','about.html','.nojekyll']:
 if not (DOC/x).exists():errors.append('Missing publication entry '+x)
print(f"Checked {len(manifest['papers'])} papers, {len(list(DOC.rglob('*.html')))} HTML pages, {len(manifest['diagrams'])} SVG diagrams")
if errors:
 print('FAILED:')
 for e in errors[:80]:print(' -',e)
 print(len(errors),'total failures')
 sys.exit(1)
print('OK — all source hashes and local links verified')
