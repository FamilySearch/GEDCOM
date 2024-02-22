from sys import argv
from os.path import join, dirname, isfile, isdir, exists
from os import makedirs

def get_paths():
    """Parses command-line arguments, if present; else uses defaults"""
    spec = [_ for _ in argv[1:] if isfile(_)]
    dest = [_ for _ in argv[1:] if isdir(_)]
    if len(dest) != 1: raise Exception("One destination expected, but got "+str(dest))
    if len(spec) < 1: raise Exception("Expected input files, none given")
    
    return spec, dest[0]


if __name__ == '__main__':
    srcs, dst = get_paths()
    abnf = []
    gedstruct = []
    where = None
    header = ''
    for src in srcs:
        with open(src) as f:
            for line in f:
                if line.startswith('```'):
                    if where:
                        if where == 'abnf': abnf.append('\n\n')
                        elif where == 'gedstruct': gedstruct.append('\n\n')
                        where = None
                    elif 'gedstruct' in line:
                        where = 'gedstruct'
                        if header:
                            gedstruct.append(header.replace('`', '') + '\n')
                            header = ''
                    elif 'abnf' in line:
                        where = 'abnf'
                        if header:
                            abnf.append('; ' + '-'*13 + ' '  +header + ' ' + '-'*13 + '\n\n')
                            header = ''
                elif where == 'abnf': abnf.append(line)
                elif where == 'gedstruct': gedstruct.append(line)
                elif line.startswith('#'):
                    header = line
                    if '{' in header: header = header[:header.find('{')]
                    header = header.strip('# \n\r\t')
    with open('languagetag.abnf') as f:
        abnf.append(f.read())
    with open('mediatype.abnf') as f:
        abnf.append(f.read())
    with open('core.abnf') as f:
        abnf.append(f.read())
    with open(join(dst,'grammar.abnf'), 'w') as f:
        f.write('''; This document is in ABNF, see <https://tools.ietf.org/html/std68>
; This document uses RFC 7405 to add case-sensitive literals to ABNF.

''')
        f.write(''.join(abnf))
    with open(join(dst,'grammar.gedstruct'), 'w') as f:
        f.write(''.join(gedstruct))
