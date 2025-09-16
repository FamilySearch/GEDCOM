import re
import sys

if len(sys.argv) < 3:
    print("USAGE:",argv[0],"input.html output.html", sys.stderr)
    sys.exit(1)

src = sys.argv[1]
dst = sys.argv[2]




with open(src) as fh:
    doc = fh.read()

# remove col and colgroup elements, which confuse some HTML rendering engines
doc = re.sub(r'</?col[^>]*>','',doc)

# find header IDs
targets = re.findall(r'<h[^>]*id="([^"]*)"', doc)
special = {a[1]:a[0] for a in re.findall(r'<a href="#([^"]*)"[^>]*></a><span class="va">([A-Z][A-Za-z]*)</span>', doc)}

# find tags in tables (individual events, etc)
table_tags = {}
for table in re.finditer(r'<h\d[^>]*id="([^"]*)".*?<table>(.*?)</table>', doc):
    anchor, body = table.groups()
    if '<th>Tag</th>' in body:
        for tag in re.findall(r'<td><code>([^<]*)</code></td>', body):
            table_tags[tag] = anchor

def anchorify(m):
    full = m.group(0)
    tag = m.group(1)
    tag2 = m.groups()[-1].replace('#','-')
    if tag2 in targets:
        full = full.replace(tag, '<a href="#'+tag2+'">'+tag+'</a>')
    elif tag2 in special:
        full = full.replace(tag, '<a href="#'+special[tag2]+'">'+tag+'</a>')
    elif tag2 in table_tags:
        full = full.replace(tag, '<a href="#'+table_tags[tag2]+'">'+tag+'</a>')
    elif tag2.lower().replace(' ','-') in targets:
        full = full.replace(tag, '<a href="#'+tag2.lower().replace(' ','-')+'">'+tag+'</a>')
    return full

doc = re.sub(r'<code>(g7:[^<]*)</code></h', r'<code class="uri">\1</code></h', doc)
doc = re.sub(r'<code>(g7.1:[^<]*)</code></h', r'<code class="uri">\1</code></h', doc)

chunks = re.split(r'(<pre[^>]*ged(?:struct|com)[^>]*>.*?</pre>)', doc, flags=re.DOTALL)

# to do: find anchors for n @XREF:...@ and link tag @XREF:...@ to them
# to do: make code links to table tag definitions

with open(dst, 'w') as to:
    for i in range(len(chunks)):
        txt = chunks[i]
        if (i&1):
            # txt = re.sub(r'<span class="fu">\s*([^ <]+)\s*</span>', anchorify, txt)
            txt = re.sub(r'<span class="kw">\s*&lt;&lt;([^ &]+)&gt;&gt;\s*</span>', anchorify, txt)
            txt = re.sub(r'<span class="at">(g7:([^<]+))</span>', anchorify, txt)
            txt = re.sub(r'&lt;([A-Z][a-z][A-Za-z ]+)(?:&gt;|:)', anchorify, txt)
            txt = re.sub(r':([A-Z][a-z][A-Za-z ]+)&gt;', anchorify, txt)
        to.write(txt)
