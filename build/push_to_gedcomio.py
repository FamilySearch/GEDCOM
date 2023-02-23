from glob import glob
from sys import argv, stderr
from os.path import dirname, isdir, join, getmtime, basename, exists
from os import makedirs, utime
from shutil import copyfile

def get_paths():
    """Parses command-line arguments, if present; else uses defaults"""
    src = join(dirname(argv[0]),'../extracted-files/tags')
    doc = join(dirname(argv[0]),'../specification')
    if len(argv) == 4:
        doc, src, dst = argv[1:]
    if len(argv) == 3:
        src, dst = argv[1:]
    elif len(argv) == 2:
        dst = argv[1]
    else:
        raise Exception("ERROR: Must specify path to local clone of gedcom.io repository on command line")
    if not isdir(src):
        raise Exception("ERROR: Source directory "+repr(src)+" is not a directory")
    if not isdir(join(dst, '.git')):
        raise Exception("ERROR: Destination directory "+repr(dst)+" is not git repostory")
    dst = join(dst, '_pages', 'tag-def')
    if not isdir(dst):
        makedirs(dst)

    return doc, src, dst

try:
    doc, src, dst = get_paths()
except Exception as ex:
    print(str(ex), file=stderr)
    print("  USAGE:", argv[0], "[[tag/yamls/] specs/]", "local/clone/of/gedcom.io/", file=stderr)
    exit(1)

for yaml in glob(join(src,'*')):
    term = basename(yaml)
    ofile = join(dst, term+'.md')
    if exists(ofile) and getmtime(ofile) == getmtime(yaml):
        continue
    print('  updating', term)
    with open(ofile, 'w') as o:
        print('''---
title: {0}
permalink: /terms/v7/{0}.html
layout: none
redirect-from:
  - /terms/v7/{0}
...

```
'''.format(term), file=o)
        with open(yaml) as i: o.write(i.read())
        print('''
```''', file=o)
    utime(ofile, (getmtime(yaml),getmtime(yaml)))

pdf = join(doc,'gedcom.pdf'), join(dst,'../../specifications','FamilySearchGEDCOMv7.pdf')
html = join(doc,'gedcom.html'), join(dst,'../../specifications','FamilySearchGEDCOMv7.html')
for f,t in pdf, html:
    if exists(f) and (not exists(t) or getmtime(t) < getmtime(f)):
        print('Updating', basename(t))
        copyfile(f, t)
        utime(t, (getmtime(f), getmtime(f)))


with open(join(doc,'..','changelog.md')) as cl_new:
    with open(join(dst,'..','changelog.md'), 'w') as cl_old:
        print('''---
        title: FamilySearch GEDCOM Changelog
        permalink: /changelog/
        sidebar:
        nav: "changelog"
        ---''', file=cl_old)
        for line in cl_new:
           cl_old.write(line)

