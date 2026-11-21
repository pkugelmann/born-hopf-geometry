#!/usr/bin/env python3
"""Regenerate 31-paper current-source AUX aliases from canonical AUX.

Run after compiling all edited TeX files into current xref/<stem>.aux.
Old alias *names* are retained solely for cross-reference compatibility.
"""
import pathlib,re,hashlib,json,sys
r=pathlib.Path(sys.argv[1]).resolve() if len(sys.argv)>1 else pathlib.Path(__file__).resolve().parent
roots={}
for p in sorted(r.glob('Paper[1-7][A-G]-*.tex')):
 code=re.match(r'(Paper\d+[A-G])-',p.name).group(1)
 assert code not in roots,code
 roots[code]=p.stem
assert len(roots)==31
xref=r/'xref';xref.mkdir(exist_ok=True)
entries=[]
for p in sorted(xref.glob('Paper[1-7][A-G]-*.aux')):
 code=re.match(r'(Paper\d+[A-G])-',p.name).group(1)
 if code not in roots: continue
 current=xref/(roots[code]+'.aux');assert current.is_file()
 p.write_bytes(current.read_bytes())
for code,stem in sorted(roots.items()):
 source=(xref/(stem+'.aux')).read_bytes()
 for alias in sorted(xref.glob(code+'-*.aux')):
  entries.append({'logical_paper':code,'xref_name':alias.name,'current_source':stem+'.tex',
  'sha256':hashlib.sha256(source).hexdigest(),'compatibility_alias':alias.stem!=stem})
(r/'Paper00-XrefAliasManifest-v1_36.json').write_text(json.dumps({'current_papers':31,'entries':entries,
'note':'Aliases carry currently compiled AUX bytes, not historical proof versions.'},indent=2)+'\n')
print('Current-source AUX alias set:',len(entries))
