#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

import argparse

parser = argparse.ArgumentParser(description='Enforce specific dungeon types')
parser.add_argument('dungeon',
    type=str,
    nargs='+',
    metavar='dungeon',
    help='dungeon ID(s) to spawn',
    )
parser.add_argument('-d', '--disable',
    action='store_true',
    help='Disable the mod so it doesn\'t actualy do anything')
args = parser.parse_args()

# NOTE: Does not do anything to ocean/toxic/arctic/magma worlds
planet_types = [
        'garden',
        'forest',
        'desert',
        'savannah',
        'snow',
        'jungle',
        'alien',
        'tundra',
        'midnight',
        'volcanic',
        'scorchedcity',
        ]

# Dungeon counts
dungeon_counts = {
        'verysmall': (3, 3),
        'small': (3, 3),
        'medium': (3, 6),
        'large': (6, 9),
        }

# Construct our dungeon list
dungeon_list = '[{}]'.format(', '.join(['[1.0, "{}"]'.format(d) for d in args.dungeon]))

# Figure out our op
if args.disable:
    op = 'test'
else:
    op = 'replace'

# Now write out the mod
filename = 'terrestrial_worlds.config.patch'
with open(filename, 'w') as df:
    print('[', file=df)
    for size, (dmin, dmax) in dungeon_counts.items():
        print('    {', file=df)
        print('        "op": "{}",'.format(op), file=df)
        print('        "path": "/planetSizes/{}/layerDefaults/dungeonCountRange",'.format(size), file=df)
        print('        "value": [{}, {}]'.format(dmin, dmax), file=df)
        print('    },', file=df)
    for idx, planet in enumerate(planet_types):
        if idx == len(planet_types)-1:
            comma = ''
        else:
            comma = ','
        print('    {', file=df)
        print('        "op": "{}",'.format(op), file=df)
        print('        "path": "/planetTypes/{}/layers/surface/dungeons",'.format(planet), file=df)
        print('        "value": {}'.format(dungeon_list), file=df)
        print('    }}{}'.format(comma), file=df)
    print(']', file=df)

# Report
print('Wrote info for {} biomes to {}'.format(len(planet_types), filename))
if args.disable:
    print('(mod is actually inactive, though)')
