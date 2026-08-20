import json
from pathlib import Path
from pprint import pprint

RUTA = Path(__file__).resolve().parent

with open(RUTA / "1-mi-json.json", encoding="utf-8") as archivo:
    datos = json.load(archivo)

pprint(datos)
