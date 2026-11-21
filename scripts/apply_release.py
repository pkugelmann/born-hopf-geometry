#!/usr/bin/env python3
"""Install a versioned Born–Hopf website payload into an existing Git clone.
Only explicitly managed directories/files are replaced; Git history and all
unrelated repository files are left intact. Run via publish.sh.
"""
import argparse,pathlib,shutil,sys
MANAGED_DIRS=['docs','content','scripts','.github/workflows','.github/ISSUE_TEMPLATE']
MANAGED_FILES=['README.md','GITHUB-SETUP.md','RELEASE-ORIGINALS.md','CHANGELOG.md',
               'CITATION.cff','requirements-edit.txt','.gitignore','.gitattributes','publish.sh']

def apply(source,target):
    source=source.resolve();target=target.resolve()
    if source==target or source in target.parents or target in source.parents:
        raise ValueError('Source must be separate from the target Git clone')
    if not (target/'.git').is_dir():raise ValueError('Target is not an existing Git worktree')
    if not (source/'docs/data/manifest.json').is_file():raise ValueError('Source website manifest missing')
    for rel in MANAGED_DIRS:
        src=source/rel;dest=target/rel
        if not src.is_dir():raise ValueError('Missing managed directory: '+rel)
        if dest.is_symlink():raise ValueError('Refusing to replace symlink: '+rel)
        if dest.exists():shutil.rmtree(dest)
        dest.parent.mkdir(parents=True,exist_ok=True)
        shutil.copytree(src,dest,symlinks=False)
    for rel in MANAGED_FILES:
        src=source/rel;dest=target/rel
        if not src.is_file():raise ValueError('Missing managed file: '+rel)
        if dest.is_symlink():raise ValueError('Refusing to replace symlink: '+rel)
        dest.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(src,dest)
    print('Replaced managed site/content/scripts/workflows; preserved all other repository files and .git history.')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('target')
    a=p.parse_args();apply(pathlib.Path(a.source),pathlib.Path(a.target))
