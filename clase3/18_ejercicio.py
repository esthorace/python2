"""
# Convertir a POO

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def escribir_archivo(ruta: str, contenido: str) -> None:
    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(contenido)j
            logging.debug("✅ Archivo escrito exitosamente")
    except PermissionError:
        logging.error("No hay permisos para escribir.")
    except Exception as error:
        logging.critical("Error inesperado:", repr(error))


def leer_archivo(ruta: str) -> str | None:
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            logging.info("✅ Archivo leído exitosamente")
            return contenido
    except FileNotFoundError:
        logging.error("El archivo no existe")
    except Exception as error:
        logging.critical("Error inesperado", repr(error))


escribir_archivo("17_test.txt", "Python\nDjango\n")
texto = leer_archivo("17_test.txt")
if texto is not None:
    print(texto)
"""

import logging


class GestorArchivos:
    def __init__(self, nombre: str):
        self.nombre = nombre
        logging.basicConfig(
            level=logging.DEBUG, format="%(asctime)s - %(levelname)s: %(message)s"
        )

    def escribir_archivo(self, contenido: str):
        try:
            with open(self.nombre, "w", encoding="utf-8") as archivo:
                archivo.write(contenido)
                logging.debug(f"✅ Archivo '{self.nombre}' escrito exitosamente")
        except PermissionError:
            logging.error(f"No hay permisos para escribir '{self.nombre}'")
        except Exception as error:
            logging.critical(
                f"Error inesperado al escribir '{self.nombre}':", repr(error)
            )

    def leer_archivo(self):
        try:
            with open(self.nombre, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                logging.info(f"✅ Archivo {self.nombre} leído exitosamente")
                return contenido
        except FileNotFoundError:
            logging.error(f"El archivo {self.nombre} no existe")
        except Exception as error:
            logging.critical(f"Error inesperado al leer '{self.nombre}':", repr(error))


gestor = GestorArchivos("18_test.txt")
gestor.escribir_archivo("Python\nDjango\n")
texto = gestor.leer_archivo()
if texto is not None:
    print(texto)
