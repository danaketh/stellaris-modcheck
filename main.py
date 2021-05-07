## Stellaris ModCheck

import os
import sqlite3
import json
import re

base_path = os.path.expanduser('~/Documents/Paradox Interactive/Stellaris')
export = {
    'name': '',
    'playsets': [],
    'mods': []
}

with open(base_path + '/settings.txt') as reader:
    s = re.search('name="(.+?)"', reader.read())
    if s:
        export['name'] = s.group(1)

# Tables: mods, mods_dependencies, playsets, playsets_mods
db = sqlite3.connect(base_path + '/launcher-v2.sqlite')
cursor = db.cursor()

# Get playsets
cursor.execute("SELECT id, name, loadOrder FROM playsets")

for playset in cursor.fetchall():
    export['playsets'].append({
        'id': playset[0],
        'name': playset[1],
        'load_order': playset[2]
    })

cursor.execute("""SELECT psm.playsetId, psm.modId, psm.position, psm.enabled, m.steamId,
               m.displayName, m.thumbnailUrl, m.version, m.requiredVersion, m.tags, m.status,
               m.timeUpdated, m.size FROM playsets_mods AS psm
               LEFT JOIN mods m ON m.id = psm.modId""")

for mod in cursor.fetchall():
    export['mods'].append({
        'id': mod[1],
        'playset_id': mod[0],
        'position': mod[2],
        'enabled': mod[3],
        'steam_id': mod[4],
        'name': mod[5],
        'thumbnail_url': mod[6],
        'version': mod[7],
        'game_version': mod[8],
        'tags': mod[9],
        'status': mod[10],
        'updated_at': mod[11],
        'size': mod[12]
    })

db.close()

with open('playsets.json', 'w') as fp:
    json.dump(export, fp)

fp.close()
