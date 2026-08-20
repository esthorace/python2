import json
from pathlib import Path

RUTA = Path(__file__).resolve().parent

# lectura
with open(RUTA / "1-mi-json.json", encoding="utf-8") as archivo:
    datos: list[dict] = json.load(archivo)

# más datos
persona_nueva = {"active": None, "age": 20, "city": "Luján", "name": "Luz"}
datos.append(persona_nueva)

# escritura
with open(RUTA / "1-mi-json.json", "w", encoding="utf-8") as archivo:
    json.dump(datos, archivo, indent=4, ensure_ascii=False)
