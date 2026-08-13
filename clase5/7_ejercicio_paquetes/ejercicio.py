from dataclasses import dataclass


@dataclass
class Libro:
    titulo: str
    autor: str
    año: int


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
        for libro in biblioteca.libros:
            print(f"🪶 {libro.titulo} ✨ {libro.autor} 👌 {libro.año}")


libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943)
libro2 = Libro("1984", "George Orwell", 1949)
libro3 = Libro("Órganon", "Aristóteles", -384)

biblioteca = Biblioteca(nombre="La Gran Biblioteca")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
biblioteca.listar_libros()
biblioteca.eliminar_libro(libro3)
biblioteca.eliminar_libro(libro3)  # ✖️ El 'Órganon' no está en la biblioteca
biblioteca.listar_libros()
