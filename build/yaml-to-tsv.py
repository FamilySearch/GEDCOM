if __name__ != '__main__':
  raise Exception("This file is a script, not a library, and should not be imported")

import yaml
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="Create TSV files from a set of GEDCOM 7 YAML files")
parser.add_argument('yamldir', type=Path, nargs='+', help="The directories containing the YAML files")
parser.add_argument('--dest', required=True, type=Path, help="The directory in which to create the .tsv files")
args = parser.parse_args()

if not args.dest.is_dir():
  print("Error: --dest must be a directory")
  quit(1)

for p in args.yamldir:
  if not p.is_dir():
    print("Error:",p,"is not a directory")
    quit(1)

data = {}
for p in args.yamldir:
  for y in p.glob('*'):
    if not y.is_file(): continue
    try:
      obj = yaml.safe_load(y.open())
      data[obj['uri']] = obj
    except:
      print('Skipping non-YAML', y)


# This script checks bidirectional links because extensions might have e.g. a superstructure link without the matching substructure

# cardinalities: (superstructure, substructure, cardinality)
rows = {}
for uri,obj in data.items():
  if obj['type'] == 'structure':
    for sup,card in obj['superstructures'].items():
      rows[(sup, uri)] = card
    for sub,card in obj['substructures'].items():
      if rows.get((uri, sub),card) != card:
        raise Error(f"{uri} and {sub} disagree about their mutual cardinality")
      rows[(uri, sub)] = card
with open(Path(args.dest, "cardinalities.tsv"), 'w') as dst:
  for row in sorted([k+(v,) for k,v in rows.items()]):
    print('\t'.join(row), file=dst)

# enumeration values: (enumset, enum)
rows = set()
for uri,obj in data.items():
  if obj['type'] == 'enumeration set':
    for u in obj['enumeration values']:
      rows.add((uri,u))
  if 'vaue of' in obj:
    for u in obj['value of']:
      rows.add((u,uri))
with open(Path(args.dest, "enumerationsets.tsv"), 'w') as dst:
  for row in sorted(rows):
    print('\t'.join(row), file=dst)


# enumeration set of structures: (structure, enumset)
rows = set()
for uri,obj in data.items():
  if obj['type'] == 'structure' and 'enumeration set' in obj:
    rows.add((uri, obj['enumeration set']))
with open(Path(args.dest, "enumerations.tsv"), 'w') as dst:
  for row in sorted(rows):
    print('\t'.join(row), file=dst)


# payloads: (structure, payload type)
rows = set()
for uri,obj in data.items():
  if obj['type'] == 'structure':
    rows.add((uri, obj['payload'] or ''))
with open(Path(args.dest, "payloads.tsv"), 'w') as dst:
  for row in sorted(rows):
    print('\t'.join(row), file=dst)


# substructures: (super, tag, sub)
rows = set()
for uri,obj in data.items():
  if obj['type'] == 'structure':
    for sup,card in obj['superstructures'].items():
      if 'standard tag' in obj:
        rows.add((sup, obj['standard tag'], uri))
      for tag in obj.get('extension tags',[]):
        rows.add((sup, tag, uri))
    if len(obj['superstructures']) == 0:
      if 'standard tag' in obj:
        rows.add(('', obj['standard tag'], uri))
      for tag in obj.get('extension tags',[]):
        rows.add(('', tag, uri))
    for sub,card in obj['substructures'].items():
      if 'standard tag' in data[sub]:
        rows.add((uri, data[sub]['standard tag'], sub))
      for tag in data[sub].get('extension tags',[]):
        rows.add((uri, tag, sub))
with open(Path(args.dest, "substructures.tsv"), 'w') as dst:
  for row in sorted(rows):
    print('\t'.join(row), file=dst)

quit(0)




# 12.f: superstructure tag substructure
with open(Path(args.dest, "substructures.tsv"), 'w') as dst:
  for uri,s in sorted(data.items()):
    if isinstance(s, StructData):
      for sup,card in sorted(s.sup.items()):
        print(f'{sup}\t{s.tag}\t{uri}', file=dst)
      if len(s.sup) == 0:
        print(f'\t{s.tag}\t{uri}', file=dst)
