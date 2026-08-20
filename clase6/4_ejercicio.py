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


def introducir_datos() -> dict | None:
    nombre = input("Nombre: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío. Operación cancelada.")
        return None

    edad = int(input("Edad: "))
    if edad is None or edad < 0:
        print("La edad no es válida. Operación cancelada.")
        return None

    activo = input("¿Activo? ").strip() in {"s", "sí", "si"}
    return {"nombre": nombre, "edad": edad, "activo": activo}


def main() -> None:
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
    archivo = Path("4-ejercicio.json")
    usuarios = leer_json(archivo)
    nuevo_usuario = introducir_datos()
    if nuevo_usuario:
        usuarios.append(nuevo_usuario)
        print(usuarios)
        # escribir_datos(archivo, usuarios)


if __name__ == "__main__":
    main()
