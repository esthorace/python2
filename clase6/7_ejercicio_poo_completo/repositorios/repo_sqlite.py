import logging
import sqlite3
from pathlib import Path

from .repositorio import RepositorioUsuarios

logger = logging.getLogger(__name__)


class RepositorioUsuariosSQLite(RepositorioUsuarios):
    def __init__(self, ruta: Path) -> None:
        self.ruta = ruta
        self._crear_tabla()

    def _crear_tabla(self) -> None:
        try:
            with sqlite3.connect(self.ruta) as conexion:
                conexion.execute(
                    """
                    CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        edad INTEGER NOT NULL,
                        activo INTEGER NOT NULL
                    )
                    """
                )
        except sqlite3.Error:
            logger.exception("Error al crear la tabla de usuarios")
            raise

    def leer_datos(self) -> list:
        try:
            with sqlite3.connect(self.ruta) as conexion:
                conexion.row_factory = sqlite3.Row
                filas = conexion.execute(
                    "SELECT nombre, edad, activo FROM usuarios"
                ).fetchall()
        except sqlite3.Error:
            logger.exception("Error al leer los usuarios")
            return []

        return [
            {
                "nombre": fila["nombre"],
                "edad": fila["edad"],
                "activo": bool(fila["activo"]),
            }
            for fila in filas
        ]

    def escribir_datos(self, datos: list) -> None:
        try:
            with sqlite3.connect(self.ruta) as conexion:
                # conexion.execute("DELETE FROM usuarios")
                conexion.executemany(
                    "INSERT INTO usuarios (nombre, edad, activo) VALUES (?, ?, ?)",
                    [(u["nombre"], u["edad"], int(u["activo"])) for u in datos],
                )
        except sqlite3.Error:
            logger.exception("Error al escribir los usuarios")
            raise

    def agregar_datos(self, usuario: dict) -> None:
        try:
            with sqlite3.connect(self.ruta) as conexion:
                conexion.execute(
                    "INSERT INTO usuarios (nombre, edad, activo) VALUES (?, ?, ?)",
                    (usuario["nombre"], usuario["edad"], int(usuario["activo"])),
                )
        except sqlite3.Error:
            logger.exception("Error al agregar el usuario")
            raise
