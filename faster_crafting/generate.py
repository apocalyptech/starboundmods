#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

import os
import json

source_path = '/usr/local/games/Steam/SteamApps/common/Starbound/assets/cjunpacked/recipes'
target_path = '/usr/local/games/Steam/SteamApps/common/Starbound/mods/faster_crafting/recipes'

if not os.path.exists(source_path):
    raise Exception('Update source_path so that it exists')

# Some of these can't actually be parsed as JSON, but thankfully
# we wouldn't be doing anything with 'em anyway.
blacklist = set([
    'heartforge.recipe',
    'holidaycraftingtable.recipe',
    'kennel.recipe',
    ])

replace_count = 0
add_count = 0
os.chdir(source_path)
for (dirpath, dirnames, filenames) in os.walk('.'):
    for filename in filenames:
        if filename in blacklist:
            continue
        if filename.endswith('.recipe'):
            with open(os.path.join(dirpath, filename), 'r') as df:
                data = json.load(df)
                new_path = os.path.join(target_path, dirpath)
                new_file = os.path.join(new_path, '{}.patch'.format(filename))
                if 'duration' in data:
                    if data['duration'] > 0.05:
                        os.makedirs(new_path, exist_ok=True)
                        with open(new_file, 'w') as odf:
                            print('[', file=odf)
                            print('    {', file=odf)
                            print('        "op": "replace",', file=odf)
                            print('        "path": "/duration",', file=odf)
                            print('        "value": 0.05', file=odf)
                            print('    }', file=odf)
                            print(']', file=odf)
                            replace_count += 1
                else:
                    os.makedirs(new_path, exist_ok=True)
                    with open(new_file, 'w') as odf:
                        print('[', file=odf)
                        print('    {', file=odf)
                        print('        "op": "add",', file=odf)
                        print('        "path": "/duration",', file=odf)
                        print('        "value": 0.05', file=odf)
                        print('    }', file=odf)
                        print(']', file=odf)
                        add_count += 1
print('Wrote {} files: {} replacements, {} additions'.format(replace_count+add_count, replace_count, add_count))


