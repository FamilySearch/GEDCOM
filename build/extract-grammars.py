from sys import argv
from os.path import join, dirname, isfile, isdir, exists
from os import makedirs

def get_paths():
    """Parses command-line arguments, if present; else uses defaults"""
    spec = join(dirname(argv[0]),'../GEDCOM.md') if len(argv) < 2 or not isfile(argv[1]) else argv[1]
    dest = join(dirname(argv[0]),'../')
    for arg in argv:
        if arg and isdir(arg):
            dest = arg
            break
        if arg and not exists(arg) and arg[0] != '-' and isdir(dirname(arg)):
            dest = arg
            break

    if not isdir(dest):
        makedirs(dest)
    
    return spec, dest


if __name__ == '__main__':
    src, dst = get_paths()
    abnf = []
    gedstruct = []
    where = None
    header = ''
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
    with open(join(dst,'grammar.abnf'), 'w') as f:
        f.write('''; This document is in ABNF, see <https://tools.ietf.org/html/std68>
; This document uses RFC 7405 to add case-sensitive literals to ABNF.

''')
        f.write(''.join(abnf))
    with open(join(dst,'grammar.gedstruct'), 'w') as f:
        f.write(''.join(gedstruct))
