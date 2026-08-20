"""
Simulación de base de datos JSON
1. Leer el archivo JSON
2. Pedir al usuario que introduzca más datos (input)
3. Guardar el archivo JSON

Usar with, try-except, logging, funciones
"""

import json
import logging
from pathlib import Path

RUTA = Path(__file__).resolve().parent
logger = logging.getLogger(__name__)


def leer_json(ruta: Path) -> list:
    try:
        with ruta.open("r", encoding="utf-8") as f:
            datos = json.load(f)
    except FileNotFoundError:
        logger.warning("El archivo no existe")
        return []
    except json.JSONDecodeError:
        logger.exception("El archivo existe pero está corrupto")
        return []
    except OSError:
        logger.exception("Error de E/S al leer el archivo")
        return []
    else:
        if not isinstance(datos, list):
            logger.warning("El contenido no es una lista")
            return []
        return datos


def main() -> None:
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
    archivo = Path("4-ejercicio.json")
    usuarios: list[dict] = leer_json(archivo)
    print(usuarios)
    print(type(usuarios))


if __name__ == "__main__":
    main()
