import logging
from pathlib import Path

from repositorios.repo_json import RepositorioUsuariosJSON

# from repositorios.repo_sqlite import RepositorioUsuariosSQLite

RUTA = Path(__file__).resolve().parent
logger = logging.getLogger(__name__)


class GestorUsuarios:
    def __init__(self, repositorio) -> None:
        self.repositorio = repositorio

    def introducir_datos(self) -> dict | None:
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

    def agregar_usuario(self) -> None:
        usuarios = self.repositorio.leer_datos()
        nuevo_usuario = self.introducir_datos()
        if nuevo_usuario:
            usuarios.append(nuevo_usuario)
            self.repositorio.escribir_datos(usuarios)


def main() -> None:
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
    gestor = GestorUsuarios(RepositorioUsuariosJSON(Path("db.json")))
    # gestor = GestorUsuarios(RepositorioUsuariosSQLite(Path("db.sqlite")))
    gestor.agregar_usuario()


if __name__ == "__main__":
    main()
