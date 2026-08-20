import json
import logging
from pathlib import Path

RUTA = Path(__file__).resolve().parent
logger = logging.getLogger(__name__)


class RepositorioUsuarios:
    def __init__(self, ruta: Path) -> None:
        self.ruta = ruta

    def leer_datos(self) -> list:
        try:
            with self.ruta.open("r", encoding="utf-8") as f:
                datos = json.load(f)
        except FileNotFoundError:
            logger.warning("El archivo no existe")
            return []
        except json.JSONDecodeError:
            logger.exception("El archivo existe pero está corrupto")
            raise
        except OSError:
            logger.exception("Error de E/S al leer el archivo")
            return []
        else:
            if not isinstance(datos, list):
                logger.warning("El contenido no es una lista")
                return []
            return datos

    def escribir_datos(self, datos: list) -> None:
        try:
            with self.ruta.open("w", encoding="utf-8") as f:
                json.dump(datos, f, indent=4, ensure_ascii=False)
                logger.info("Datos guardados correctamente en %s", self.ruta)
        except OSError:
            logger.error("Error de E/S al escribir el archivo.")
            raise
