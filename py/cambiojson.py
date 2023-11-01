import json
import os

#URL CARPETA DE JSONS
carpeta = 'URL DEL ARCHIVO JSON'

combined_data = []

for archivo in os.listdir(carpeta):
    if archivo.endswith('.json'):
        with open(os.path.join(carpeta, archivo), 'r') as f:
            data = json.load(f)
        combined_data.append(data)

with open('train.json', 'w') as f:
    json.dump(combined_data, f, indent=4)
