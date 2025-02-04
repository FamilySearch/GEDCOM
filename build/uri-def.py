import re
from sys import argv, stderr
from os.path import isfile, isdir, exists, dirname, join, basename
from os import makedirs
from subprocess import run
from shutil import copyfile
from glob import glob


def get_paths():
    """Parses command-line arguments, if present; else uses defaults"""
    spec = [_ for _ in argv[1:] if isfile(_)]
    dest = [_ for _ in argv[1:] if isdir(_)]
    if len(dest) != 1: raise Exception("One destination expected, but got "+str(dest)+"\nUSAGE: "+argv[0]+" input1.md input2.md destination/")
    if len(spec) < 1: raise Exception("Expected input files, none given"+"\nUSAGE: "+argv[0]+" input1.md input2.md destination/")
    
    return spec, dest[0]

def get_text(spec):
    """Reads the contents of the given file"""
    return '\n\n'.join(open(s).read() for s in spec)

def get_prefixes(txt):
    """Find and parse prefix definition tables"""
    pfx = {}
    for pfxtable in re.finditer(r'([^\n]*)Short Prefix *\| *URI Prefix *\|(\s*\|[^\n]*)*', txt):
        for abbr, lng in re.findall(r'`([^`]*)` *\| *`([^`]*)`', pfxtable.group(0)):
            pfx[abbr] = lng
    return pfx

def find_data_types(txt, g7):
    """Returns datatype:uri and adds URI suffixes to g7"""
    dturi = {}
    for section in re.finditer(r'^#+ *([^\n]*)\n+((?:[^\n]|\n+[^\n#])*[^\n]*URI for[^\n]*data types? is(?:[^\n]|\n+[^\n#])*)', txt, re.M):
        for dt, uri in re.findall(r'URI[^\n]*`([^\n`]*)` data type[^\n]*`([^`\n:]*:[^\n`]*)`', section.group(0)):
            dturi[dt] = uri
            if uri.startswith('g7:'):
                if '#' in uri: uri = uri[:uri.find('#')]
                if uri[3:] not in g7:
                    g7[uri[3:]] = ('data type', [section.group(2).strip()])
    return dturi
    
def find_cat_tables(txt, g7, tagsets):
    """Looks for tables of tags preceded by a concatenation-based URI
    
    Raises an exception if any URI is repeated with distinct definitions. This code contains a hard-coded fix for BIRTH which has the same unifying concept but distinct text in the spec.
    
    Returns a {structure:[list,of,allowed,enums]} mapping
    and a {calender:[list,of,months],month:[list,of,calendars]} mapping
    """
    hard_code = { ## <- hack for enum-BIRTH
        "g7:enum-BIRTH": 'Associated with birth, such as a birth name or birth parents.',
    }
    cats = {}
    enums = {}
    calendars = {}
    for bit in re.finditer(r'by\s+concatenating\s+`([^`]*)`', txt):
        i = txt.rfind('\n#', 0, bit.start())
        j = txt.find(' ',i)
        j = txt.find(txt[i:j+1], j)
        sect = txt[i:j].replace('(Latter-Day Saint Ordinance)','`ord`') ## <- hack for ord-STAT
        for entry in re.finditer(r'`([A-Z0-9_]+)` *\| *(.*?) *[|\n]', sect):
            enum, meaning = entry.groups()
            label = None
            h1 = sect.find('\n|',sect.rfind('\n#',0,entry.start()))+1
            h2 = sect.find('\n', h1)
            header = [_.strip() for _ in sect[h1:h2].strip('| ').split('|')]
            pfx = bit.group(1)+enum
            if 'The URI of this' in meaning:
                meaning, tail = meaning.split('The URI of this')
                if meaning.endswith('<br/>'): meaning = meaning[:-5]
                pfx = tail.split('`')[1]
            meaning = hard_code.get(pfx,meaning)
            if len(header) > 2:
                h1 = sect.rfind('\n',0,entry.start())
                h2 = sect.find('\n',h1+1)
                row = [_.strip() for _ in sect[h1:h2].strip('| \n').split('|')]
                assert len(row) == len(header)
                meaning = [(header[i]+': '+row[i] 
                if header[i] not in ('Meaning','Name')
                else row[i]) for i in range(1,len(header))]
            else:
                meaning = [meaning]
            if pfx in cats and meaning != cats[pfx]:
                raise Exception('Concatenated URI '+pfx+' has multiple definitions:'
                    + '\n    '+cats[pfx]
                    + '\n    '+meaning
                )
            if 'enum-' in pfx:
                yamltype = 'enumeration'
                k1 = sect.find('`', sect.rfind('\n#', 0, entry.start()))
                k2 = sect.rfind('`', 0, sect.find('\n', k1))
                key = sect[k1:k2].replace('`','').replace('.','-')
                if pfx not in enums.get(key,[]): enums.setdefault(key,[]).append(pfx)
            elif 'month-' in pfx:
                yamltype = 'month'
                label = re.sub(r'(,| \().*', '', meaning[0])
                k1 = sect.find('`', sect.find('URI for this calendar is', entry.start()))+1
                k2 = sect.find('`', k1)
                cal = sect[k1:k2]
                calendars.setdefault(cal,[]).append(pfx)
                calendars.setdefault(pfx,[]).append(cal)
                if 'GREGORIAN' in cal: ## <- hack for JULIAN
                    c2 = cal.replace('GREGORIAN','JULIAN')
                    calendars.setdefault(c2,[]).append(pfx)
                    calendars.setdefault(pfx,[]).append(c2)
                    
            else:
                raise Exception("unexpected enumeration URI prefix "+repr(pfx))
            if pfx not in cats:
                cats[pfx] = meaning
                if pfx.startswith('g7:'):
                    if pfx[3:] in g7:
                        raise Exception(pfx+' defined as an enumeration and a '+g7[pfx[3:]][0])
                    if label:
                        g7[pfx[3:]] = (yamltype, meaning, None, label)
                    else:
                        g7[pfx[3:]] = (yamltype, meaning)
    return enums, calendars

def find_calendars(txt, g7):
    """Looks for sections defining a `g7:cal-` URI"""
    for bit in re.finditer(r'#+ `[^`]*`[^\n]*\n+((?:\n+(?!#)|[^\n])*is `g7:(cal-[^`]*)`(?:\n+(?!#)|[^\n#])*)', txt):
        m = re.search('The epoch markers? ([`_A-Z0-9, and]+) (is|are) permitted', bit.group(1))
        marker = [] if not m else re.findall(r'[A-Z0-9_]+', m[1])
        m = re.match(r'^The ([A-Z][A-Za-z]* )+calendar', bit.group(1))
        if m:
            g7[bit.group(2)] = ('calendar',[bit.group(1)], marker, m.group(0)[4:-9])
        else:
            g7[bit.group(2)] = ('calendar',[bit.group(1)], marker)
        

def joint_card(c1,c2):
    """Given two cardinalities, combine them."""
    return '{' + ('1' if c1[1] == c2[1] == '1' else '0') + ':' + ('1' if c1[3] == c2[3] == '1' else 'M') + '}'

def parse_rules(txt):
    """returns {rule:[(card,uri),(card,uir),...] for each level-n
    production of the rule, even if indirect (via another rule),
    regardless of if alternation or set."""
    # Find gedstruct context
    rule_becomes = {}
    rule_becomes_rule = {}
    for rule,block,notes in re.findall(r'# *`([A-Z_0-9]+)` *:=\s+```+[^\n]*\n([^`]*)``+[^\n]+((?:[^\n]|\n(?!#))*)', txt):
        for card, uri in re.findall(r'^n [A-Z@][^\n]*(\{.:.\}) *(\S+:\S+)', block, re.M):
            rule_becomes.setdefault(rule,[]).append((card, uri))
        for r2, card in re.findall(r'^n <<([^>]*)>>[^\n]*(\{.:.\})', block, re.M):
            rule_becomes_rule.setdefault(rule,[]).append((card, r2))
    # Fixed-point rule-to-rule resolution
    again = True
    while again:
        again = False
        for r1,rset in tuple(rule_becomes_rule.items()):
            flat = True
            for c,r2 in rset:
                if r2 in rule_becomes_rule:
                    flat = False
            if flat:
                for c,r2 in rset:
                    rule_becomes.setdefault(r1,[]).extend((joint_card(c,c2),uri) for (c2,uri) in rule_becomes[r2])
                del rule_becomes_rule[r1]
            else:
                again = True
    return rule_becomes

def new_key(val, d, *keys, msg=''):
    """Helper method to add to a (nested) dict and raise if present"""
    for k in keys[:-1]:
        d = d.setdefault(k, {})
    if keys[-1] in d:
        if d[keys[-1]] != val:
            raise Exception(msg+'Duplicate key: '+str(keys))
    else: d[keys[-1]] = val

def parse_gedstruct(txt, rules, dtypes):
    """Reads through all gedstruct blocks to find payloads, substructures, and superstructures"""
    sup,sub,payload = {'g7:CONT':[]}, {}, {}
    for block in re.findall(r'```[^\n]*gedstruct[^\n]*\n([^`]*)\n```', txt):
        stack = []
        for line in block.split('\n'):
            parts = line.strip().split()
            if len(parts) < 3:
                if line not in ('[','|',']'):
                    raise Exception('Invalid gedstruct line: '+repr(line))
                continue
            if parts[1].startswith('@'): del parts[1]
            if parts[0] == 'n': stack = []
            else:
                n = int(parts[0])
                while n < len(stack): stack.pop()
            if parts[1].startswith('<'):
                card = parts[2]
                if len(stack):
                    for c,u in rules[parts[1][2:-2]]:
                        new_key(joint_card(card,c), sup, u, stack[-1], msg='rule sup: ')
                        new_key(joint_card(card,c), sub, stack[-1], u, msg='rule sub: ')
            else:
                uri = parts[-1]
                card = parts[-2]
                if len(parts) > 4:
                    p = ' '.join(parts[2:-2])[1:-1]
                    if p.startswith('<XREF:'): p = '@<https://gedcom.io/terms/v7/record-'+p[6:]+'@'
                    elif p == 'Y|<NULL>': pass
                    else: p = dtypes[p]
                else: p = None
                new_key(p, payload, uri, msg='payload: ')
                if len(stack):
                    new_key(card, sup, uri, stack[-1], msg='line sup: ')
                    new_key(card, sub, stack[-1], uri, msg='line sub: ')
                stack.append(uri)
    return {k:{'sub':sub.get(k,[]),'sup':sup.get(k,[]),'pay':payload.get(k)} for k in sub.keys()|sup.keys()|payload.keys()}

def find_descriptions(txt, g7, ssp):
    """Collects structure definitions as follows:
    
    - Sections '#+ TAG (Name) `g7:FULL.TAG`'
    - Sections '#+ `RULE` :=' with only one level-n struct
    - Rows in tables 'Tag | Name<br/>URI | Description'
    
    Returns a {section header:[list,of,uris]} mapping
    """
    
    # structure sections
    for name,uri,desc in re.findall(r'#+ `[^`]*`[^\n]*\(([^)]*)\)[^\n]*`([^:`\n]*:[^`\n]*)`[^\n]*\n+((?:\n+(?!#)|[^\n])*)', txt):
        if uri not in ssp:
            raise Exception('Found section for '+uri+' but no gedstruct')
        if uri.startswith('g7:'):
            g7.setdefault(uri[3:],('structure',[],ssp[uri],name.strip()))[1].extend((
                name.strip(),
                desc.strip()
            ))
            for other in re.findall(r'[Aa] type of `(\S*)`', desc):
                m = re.search('^#+ +`'+other+r'`[^\n`]*\n((?:[^\n]+|\n+(?!#))*)', txt, re.M)
                if m:
                    g7[uri[3:]][1].append(m.group(1).strip())
    
    # error check that gedstruct and sections align
    for uri in ssp:
        if uri.startswith('g7:') and uri[3:] not in g7:
            raise Exception('Found gedstruct for '+uri+' but no section')

    # gedstruct sections
    for uri, desc in re.findall(r'#+ *`[^`]*` *:=[^\n]*\n+`+[^\n]*\n+n [^\n]*\} *(\S+:\S+) *(?:\n [^\n]*)*\n`+[^\n]*\n+((?:[^\n]|\n(?!#))*)', txt):
        g7[uri[3:]][1].append(desc.strip())
    
    tagsets = {}
    # tag tables
    for table in re.finditer(r'\n#+ (\S[-A-Za-z0-9 ]*[a-z0-9])[^#]*?Tag *\| *Name[^|\n]*\| *Description[^\n]*((?:\n[^\n|]*\|[^\n|]*\|[^\n]*)*)', txt):
        pfx = ''
        header = table.group(1)
        if header.startswith('Fam'): pfx = 'FAM-'
        if header.startswith('Indi'): pfx = 'INDI-'
        for tag, name, desc in re.findall(r'`([A-Z_0-9]+)` *\| *([^|\n]*?) *\| *([^|\n]*[^ |\n]) *', table.group(2)):
            if '<br' in name:
                tag = name[name.find('`g7:')+4:name.rfind('`')]
                name = name[:name.find('<br')]
            if tag not in g7: tag = pfx+tag
            if tag not in g7:
                raise Exception('Found table for '+tag+' but no section or structure')
            if g7[tag][0] != 'structure':
                raise Exception('Found table for '+tag+' but that\'s a '+g7[tag][0]+' not a structure')
            tagsets.setdefault(header,[]).append(tag)
            g7[tag][1].append(name.strip())
            g7[tag][1].append(desc.strip())
    return tagsets

def find_enum_by_link(txt, enums, tagsets):
    """Extend enums with the tagsets suggested by any section with #enum- in the header that lacks a table and links to Events or Attributes"""
    # enums.setdefault('g7:enumset-EVENATTR',[]).extend(( ## <- hack because of table omission
            # 'g7:INDI-EVEN',
            # 'g7:FAM-EVEN',
            # 'g7:INDI-FACT',
            # 'g7:FAM-FACT',
        # ))         ## do not do for enumset-EVEN 
    for sect in re.finditer(r'# *`(g7:enumset-[^`]*)`[\s\S]*?\n#', txt):
        if '[Events]' in sect.group(0):
            key = sect.group(1).replace('`','').replace('.','-')
            for k in tagsets:
                if 'Event' in k:
                    enums.setdefault(key, [])
                    for tag in tagsets[k]:
                        tag = tag.replace('INDI-','enum-').replace('FAM-','enum-')
                        tag = 'g7:'+tag
                        if tag in enums[key]: continue
                        enums[key].append(tag)
        if '[Attributes]' in sect.group(0):
            key = sect.group(1).replace('`','').replace('.','-')
            for k in tagsets:
                if 'Attribute' in k:
                    enums.setdefault(key, [])
                    for tag in tagsets[k]:
                        tag = tag.replace('INDI-','enum-').replace('FAM-','enum-')
                        tag = 'g7:'+tag
                        if tag in enums[key]: continue
                        enums[key].append(tag)
                    # enums.setdefault(key, []).extend(_ for _ in ['g7:'+_2.replace('INDI-','enum-').replace('FAM-','enum-') for _2 in tagsets[k]] if _ not in enums.get(key,[]))

def find_enumsets(txt):
    res = {}
    for sect in re.finditer(r'# *[^\n]*?`(g7:[^`]*)`([\s\S]*?)\n#', txt):
        if 'from set `g7:enumset-' in sect.group(2):
            key = sect.group(1)
            val = re.search(r'from set `(g7:enumset-[^`]*)`', sect.group(2)).group(1)
            res[key] = val
    return res

def tidy_markdown(md, indent, width=79):
    """
    The markdown files in the specification directory use the following Markdown dialect:
    
    Part of GFM:

    - setext headers with classes like `{.unnumbered}`, unlisting marks like `{-}`, and anchors like `{#container}`
    - language-specific code blocks both <code>\`\`\`gedcom</code> and <code>\`\`\` {.gedstruct .long}</code> headers
    - markdown inside HTML between lines `<div class="example">` and `</div>` (only inside lists) and between definition list tags `<dl>`, `<dt>`, and `<dd>` (only in acknowledgements)
    - code blocks with no leading blank line
    - tables with `|---|:--|` format
    - tables with `--- | --- | ---` format
    
    Not part of GFM:

    - YAML front matter
    - divs with `:::class` headers and `:::` footers
    - automatic links with `[name of section to link to]`
    - inline code with class `1 NO MARR`{.gedcom} (used only once)
    
    pip install mdformat-gfm
    """
    global prefixes
    for k,v in prefixes.items():
        md = re.sub(r'\b'+k+':', v, md)
    
    # for now ignoring YAML frontmatter
    md = re.sub(r':::(\S+)', r'<div class="\1">\n', md) # convert ::: divs to <div>s
    md = re.sub(r':::', '\n</div>', md) # convert ::: divs to <div>s
    md = re.sub(r'\]\([^\)]*\)({[^}]*})?', ']', md) # remove links
    md = re.sub(r'`{\.\S+\}', '`', md) # remove inline code classes
      
    import mdformat
    out = mdformat.text(md, extensions={"gfm"}, options={"number":True, "wrap":width})
    
    return out.rstrip().replace('\n','\n'+' '*indent).replace('\[','[').replace('\]',']')

def yaml_str_helper(pfx, md, width=79):
    txt = tidy_markdown(md, len(pfx), width)
    if ('\n'+' '*len(pfx)+'\n') in txt: return pfx + '|\n' + ' '*len(pfx) + txt
    if ': ' in txt or txt.startswith('@'):
        if '"' in txt: return pfx + '|\n' + ' '*len(pfx) + txt
        else: return pfx+'"' + txt + '"'
    return pfx + txt

def expand_prefix(txt, prefixes):
    for key in sorted(prefixes.keys(), key=lambda x:-len(x)):
        k = key+':'
        if txt.startswith(k):
            return prefixes[key] + txt[len(k):]
    return txt

if __name__ == '__main__':
    # URI definitions
    g7 = {}
    specs, dest = get_paths()
    txt = get_text(specs)
    
    prefixes = get_prefixes(txt)
    dtypes = find_data_types(txt, g7)
    rules = parse_rules(txt)
    ssp = parse_gedstruct(txt, rules, dtypes)
    tagsets = find_descriptions(txt, g7, ssp)
    enums, calendars = find_cat_tables(txt, g7, tagsets)
    find_enum_by_link(txt, enums, tagsets)
    for k in enums:
        g7[k[3:]] =  ('enumeration set',[]) 
    enumsets = find_enumsets(txt)
    find_calendars(txt, g7)

    struct_lookup = []
    enum_lookup = []
    enumset_lookup = []
    payload_lookup = []
    cardinality_lookup = []

    for tag in g7:
        print('outputting', tag, '...', end=' ')
        maybe = join(dirname(specs[0]),'terms',tag)
        if exists(maybe):
            copyfile(maybe, join(dest,tag))
            print('by copying', maybe, '...', end=' ')
            continue
        with open(join(dest,tag), 'w') as fh:
            fh.write('%YAML 1.2\n---\n')
            print('lang: en-US', file=fh)
            print('\ntype:',g7[tag][0], file=fh)
            
            # error: type-DATE# type-List#
            uri = expand_prefix('g7:'+tag,prefixes)
            print('\nuri:', uri, file=fh)
            
            if g7[tag][0] in ('structure', 'enumeration', 'calendar', 'month'):
                ptag = re.sub(r'.*-', '', re.sub(r'-[A-Z]?[a-z].*', '', tag))
                print('\nstandard tag: '+repr(ptag), file=fh)
            
            if len(g7[tag][1]) > 0:
                print('\nspecification:', file=fh)
                for desc in g7[tag][1]:
                    print(yaml_str_helper('  - ', desc), file=fh)
            
            if len(g7[tag]) > 3:
                print('\nlabel:',repr(g7[tag][3]), file=fh)
            
            if g7[tag][0] == 'structure':
                d = g7[tag][2]
                payload = expand_prefix(d['pay'],prefixes) if d['pay'] is not None else 'null'
                if payload[0] == '@' or ': ' in payload:
                    print('\npayload: "'+payload+'"', file=fh)
                else:
                    print('\npayload:', payload, file=fh)
                payload_lookup.append([uri, payload if payload != 'null' else ''])
                if d['pay'] and 'Enum' in d['pay']:
                    setname = expand_prefix(enumsets['g7:'+tag],prefixes)
                    print('\nenumeration set: "'+setname+'"', file=fh)
                    enum_lookup.append([uri,setname])
                    # print('\nenumeration values:', file=fh)
                    # for k in sorted(enums[tag]):
                        # penum = re.sub(r'.*[-:/]', '', k)
                        # puri = expand_prefix(k,prefixes)
                        # print('  -', expand_prefix(k,prefixes), file=fh)
                        # enum_lookup.append([uri,penum,puri])
                if d['sub']:
                    print('\nsubstructures:', file=fh)
                    for k,v in sorted(d['sub'].items()):
                        print('  "'+expand_prefix(k,prefixes)+'": "'+v+'"', file=fh)
                else: print('\nsubstructures: {}', file=fh)
                if d['sup']:
                    print('\nsuperstructures:', file=fh)
                    for k,v in sorted(d['sup'].items()):
                        suri = expand_prefix(k,prefixes)
                        print('  "'+suri+'": "'+v+'"', file=fh)
                        struct_lookup.append([suri,ptag,uri])
                        cardinality_lookup.append([suri,uri,v])
                else:
                    print('\nsuperstructures: {}', file=fh)
                    struct_lookup.append(['',ptag,uri])
            elif g7[tag][0] == 'calendar':
                print('\nmonths:', file=fh)
                for k in calendars['g7:'+tag]:
                    print('  - "'+expand_prefix(k, prefixes)+'"', file=fh)
                if len(g7[tag][2]) == 0:
                    print('\nepochs: []', file=fh)
                else:
                    print('\nepochs:', file=fh)
                    for epoch in g7[tag][2]:
                        print('  -', epoch, file=fh)
            elif g7[tag][0] == 'month':
                print('\ncalendars:', file=fh)
                for k in calendars['g7:'+tag]:
                    print('  - "'+expand_prefix(k, prefixes)+'"', file=fh)
            elif g7[tag][0] == 'enumeration set':
                print('\nenumeration values:', file=fh)
                for k in enums['g7:'+tag]:
                    valname = expand_prefix(k, prefixes)
                    print('  - "'+valname+'"', file=fh)
                    enumset_lookup.append([uri, valname])
            
            # handle use in enumerations (which can include any tag type)
            is_used_by = False
            for tag2 in sorted(enums):
                if ('g7:'+tag) in enums[tag2]:
                    if not is_used_by:
                        print('\nvalue of:', file=fh)
                        is_used_by = True
                    print('  - "'+expand_prefix(tag2,prefixes)+'"', file=fh)

            print('\ncontact: "https://gedcom.io/community/"', file=fh)
            fh.write('...\n')

        print('done')
    
    for path in glob(join(dirname(specs[0]),'terms','*')):
        tag = basename(path)
        if tag not in g7:
            print('copying', tag, '...', end=' ')
            copyfile(path, join(dest,tag))
            print('done')

    if dest.endswith('/'): dest=dest[:-1]
    base = dirname(dest)
    for data,name in [
        (struct_lookup, join(base,'substructures.tsv')),
        (enum_lookup, join(base,'enumerations.tsv')),
        (enumset_lookup, join(base,'enumerationsets.tsv')),
        (payload_lookup, join(base,'payloads.tsv')),
        (cardinality_lookup, join(base,'cardinalities.tsv')),
    ]:
        print('outputting', name, '...', end=' ')
        with open(name, 'w') as f:
            for row in data:
                print('\t'.join(row), file=f)
        print('done')
