from .libros import Libro


class Biblioteca:
    def __init__(self, nombre: str) -> None:
        self.nombre: str = nombre
        self.libros: list[Libro] = []

    def agregar_libro(self, libro: Libro) -> None:
        self.libros.append(libro)

    def eliminar_libro(self, libro: Libro) -> None:
        if libro not in self.libros:
            print(f"✖️ El '{libro.titulo}' no está en la biblioteca")
            return
        self.libros.remove(libro)

    def listar_libros(self):
        print(f"\nLibros de {self.nombre}")
        for libro in self.libros:
            print(f"🪶 {libro.titulo} ✨ {libro.autor} 👌 {libro.año}")
