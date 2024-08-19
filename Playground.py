import json
from collections import OrderedDict

# JSON-Datei laden
with open('Credentials.json', 'r') as file:
    data = json.load(file, object_pairs_hook=OrderedDict)

# Gewünschte Reihenfolge der Einträge
desired_order = ['ivsr_client', 'cce', 'vds']

# Einträge in gewünschter Reihenfolge sortieren
sorted_data = OrderedDict()
for key in desired_order:
    if key in data:
        sorted_data[key] = data[key]

# Aktualisierte JSON-Datei speichern
with open('Credentials.json', 'w') as file:
    json.dump(sorted_data, file, indent=4)