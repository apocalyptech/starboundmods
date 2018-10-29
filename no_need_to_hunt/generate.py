#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

import os
import io
import json

def read_config(config_data):
    """
    Attempts to parse a starbound .config file.  These are very nearly JSON,
    but include comments prefixed by //, which isn't allowed in JSON, so
    the JSON parser fails.  https://pypi.org/project/json5/ might be able
    to parse these, actually, but as its README mentions, it is SUPER slow.
    Way slower than even the gigantic list of comment special cases below.
    """
    out_lines = []
    df = io.StringIO(config_data.decode('utf-8'))
    odf = io.StringIO()
    in_comment = False
    for line in df.readlines():
        if line.lstrip()[:2] == '/*':
            if line.rstrip()[-2:] != '*/':
                in_comment = True
        else:
            if in_comment:
                if line.lstrip()[:2] == '*/':
                    in_comment = False
            else:
                idx = line.find('//')
                if idx == -1:
                    print(line, file=odf)
                else:
                    print(line[0:idx], file=odf)
    odf.seek(0)
    return json.load(odf)

base_dir = '/usr/local/games/Steam/SteamApps/common/Starbound/assets/cjunpacked/treasure'
monster_path = os.path.join(base_dir, 'monster.treasurepools')
hunting_path = os.path.join(base_dir, 'hunting.treasurepools')
with open(monster_path, 'rb') as df:
    monster_pool = read_config(df.read())
with open(hunting_path, 'rb') as df:
    hunting_pool = read_config(df.read())

# Inject "empty" (comes from common.treasurepools, and is actually fudged a bit here)
monster_pool['empty'] = [ [1, {'pool': []}] ]

# mapping_path generated with:
# grep -r --exclude=*.png --exclude=*.ogg '"bow"' * | grep Hunting | cut -d\" -f 6,10 > huntpools.txt
# from inside the stock unpacked 'monsters' dir, and then converted the quotes to commas
pools = {}
mapping_path = 'huntpools.txt'
with open(mapping_path, 'r') as df:
    for line in df.readlines():
        (first, second) = line.strip().split(',')
        pools[first] = second

class Item(object):
    
    def __init__(self, data):
        if 'item' in data:
            self.type = 'item'
            self.item = data['item']
        else:
            self.type = 'pool'
            self.item = data['pool']
        self.weight = data['weight']

    def __repr__(self):
        return '{} ({})'.format(self.item, self.weight)

out_file = 'treasure/monster.treasurepools.patch'
with open(out_file, 'w') as odf:

    print('[', file=odf)

    for idx, (old, new) in enumerate(pools.items()):
        old_pool = monster_pool[old]
        new_pool = hunting_pool[new]
        old_drops = {}
        new_drops = {}
        for (old_id, old_dict) in old_pool:
            old_items = old_dict['pool']
            for item_data in old_items:
                item = Item(item_data)
                old_drops[item.item] = item
        for (new_id, new_dict) in new_pool:
            new_items = new_dict['pool']
            for item_data in new_items:
                item = Item(item_data)
                new_drops[item.item] = item

        print(old)
        print('  {}'.format(old_drops.values()))

        for key, item in new_drops.items():
            if key in old_drops:
                old_drops[key].weight = item.weight
            else:
                old_drops[key] = item

            # Weight action figures up a bit - x2 seems to in general
            # keep them at about the same weight that they were before,
            # in most cases, but I'm bumping up the weight by double
            # that, anyway.
            if key.endswith('af') and old_drops[key].weight < 0.01:
                old_drops[key].weight *= 4

        print('  ->')
        print('  {}'.format(old_drops.values()))
        print('')

        if old == 'empty':
            # This is just for Hemogoblins, who drop nothing by default.
            # Don't actually need to change anything.
            continue

        if idx == len(pools)-1:
            comma = ''
        else:
            comma = ','

        print('    {', file=odf)
        print('        "op": "replace",', file=odf)
        print('        "path": "/{}/0/1/pool",'.format(old), file=odf)
        print('        "value": [', file=odf)
        for inner_idx, item in enumerate(old_drops.values()):
            if inner_idx == len(old_drops)-1:
                inner_comma = ''
            else:
                inner_comma = ','
            print('            {{"weight": {}, "{}": "{}"}}{}'.format(
                item.weight,
                item.type,
                item.item,
                inner_comma,
                ), file=odf)
        print('        ]', file=odf)
        print('    }}{}'.format(comma), file=odf)

    print(']', file=odf)

print('Note that changes to monsters/walkers/hemogoblinbutt/hemogoblinbutt.monstertype')
print('are not generated automatically.')
