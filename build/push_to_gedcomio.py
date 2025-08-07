from glob import glob
from sys import argv, stderr
from os.path import dirname, isdir, join, getmtime, basename, exists
from os import makedirs, utime
from shutil import copyfile
import re

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

redirects = {} # {path: {frag: path}}
content = {} # {path: [timestamp, file_contents]}
template = '''---
title: {0}
permalink: {1}.html
layout: none
redirect-from:
  - {1}
...

```
{2}
```
'''

# find files and prep for most updates
for yaml in glob(join(src,'*')):
    term = basename(yaml)
    with open(yaml) as i: data = i.read()
    uri = re.search(r'^uri: ([^\n]*)$', data, re.M).group(1)
    path = uri[uri.find('/',uri.find('//')+2):]
    if '#' in path:
        base,frag = path.split('#')
        path = path.replace('#','-') # any other mangling would work; does not need to match filenames
        redirects.setdefault(base,{})[frag] = path
    content[path] = [getmtime(yaml), template.format(term, path, data)]


# for files with fragment collisions, add a redirect script
redirect_script = '''
<script>
const allowed_fragments = {0};
const maybe_redirect = (event) => {{
    const fragment = location.hash.substr(1)
    if (fragment in allowed_fragments && location.pathname != allowed_fragments[fragment])
        location = allowed_fragments[fragment];
}};
window.addEventListener('load', maybe_redirect);
window.addEventListener('hashchange', maybe_redirect);
</script>
'''

for path in redirects:
    if path in content:
        redirects[path][''] = path
    else:
        content[path] = [
            min(content[dst][0] for dst in redirects[path].values()),
            template.format('Incomplete URI', path, 'error: this URI is incomplete without a fragment identifier'),
        ]
    script = redirect_script.format(repr(redirects[path]))
    content[path][1] += script


# update the YAML files
for (path, [ts,txt]) in content.items():
    assert path.startswith('/terms/')
    ofile = join(dst, path[len('/terms/'):]+'.md')
    if exists(ofile) and getmtime(ofile) == ts:
        continue
    print('  updating', path)
    with open(ofile, 'w') as o: o.write(txt)
    utime(ofile, (ts,ts))

        
    


# also update the specification and changelog

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

