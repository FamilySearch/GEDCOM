import re
import sys

if len(sys.argv) < 3:
    print("USAGE:",argv[0],"input.md output.md", sys.stderr)
    sys.exit(1)

src = sys.argv[1]
dst = sys.argv[2]


def slugify(bit):
    if '`g7:' in bit:
        si = bit.rfind('`g7:')+4
        ei = bit.find('`', si)
        slug = bit[si:ei].replace('#','-')
    elif '`' in bit:
        bit = re.search('`[A-Z0-9_`.]+`', bit)
        slug = bit.group(0).replace('`','').replace('.','-')
    else:
        slug = re.sub('[^-._a-z0-9]+','-', bit.lower())
    return slug

# Step 1: find all anchors and ABNF rules
slugs = {}
abnf_rules = {}
table_tags = {}
header_row = None
with open(src) as f:
    num = 0
    inabnf = False
    for line in f:
        num += 1
        if line[0] == '#':
            if '`' in line and '{' not in line:
                slug = slugify(line.replace("'s ",'.'))
            elif '{' in line and line.find('#', line.find('{')) > 0:
                slug = line[line.rfind('#')+1:]
                slug = slug[:slug.find('}')]
            else:
                if '{' in line: line = line[:line.find('{')]
                slug = slugify(line.strip('# \n\r'))
            if slug in slugs:
                raise Exception('Duplicate slug '+slug)
            slugs[slug] = num
        elif '`abnf' in line:
            inabnf = True
        elif inabnf and '`' in line:
            inabnf = False
        elif inabnf and line[0] != ' ' and '=' in line:
            abnf_rules[line.split()[0]] = slug
        elif not inabnf:
            if header_row:
                if '|' not in line: header_row = None
                elif 'Tag' in header_row and '`' in line:
                    table_tags[line.split('`')[1]] = slug
            elif '|' in line: header_row = line

last = {}
def linkable(line, num, istable=False):
    """Finds linkable items in a line of text and adds links for them"""
    def linkify(txt, slug):
        near = abs(slugs[slug]-num) < 20 or abs(last.get(slug,-100)-num) < 20
        last[slug] = num
        if near:
            return '['+txt+'](#'+slug+'){.close}'
        else:
            return '['+txt+'](#'+slug+')'
        
    def repl(m):
        slug = slugify(m.group(0))
        if slug in slugs:
            return linkify(m.group(0), slug)
        return m.group(0)
    def abnf(m):
        if m.group(1) in abnf_rules:
            slug = abnf_rules[m.group(1)]
            return linkify(m.group(0), slug)
        if m.group(1) in table_tags:
            slug = table_tags[m.group(1)]
            return linkify(m.group(0), slug)
        return m.group(0)
    uried = re.sub(r'(?<![\[.`])`g7:[-A-Z0-9`._#]+`', repl, line)
    if istable: return uried
    tagged = re.sub(r'(?<![\[.`])`[A-Z0-9`._#]+`', repl, uried)
    abnfed = re.sub(r'(?<![\[.`])`([A-Za-z0-9]+)`', abnf, tagged)
    return abnfed

# Step 2: add {#anchors} for tags; add hyperlinks
with open(src) as f:
    with open(dst,'w') as to:
        num = 0
        for line in f:
            num += 1
            if line[0] == '#':
                if '`' in line and '{' not in line:
                    slug = slugify(line.replace("'s ",'.'))
                    print(line.strip(), '{- #'+slug+'}',  file=to)
                else:
                    to.write(line)
            elif '|' in line:
                to.write(linkable(line, num, True))
                # to.write(line)
            else:
                to.write(linkable(line, num))

# Step 3 is adding links inside gedstruct code blocks. This cannot be done in markdown, so it is handled by a separate processor for the HTML
