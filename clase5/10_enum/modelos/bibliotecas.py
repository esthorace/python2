from .libros import EstadoLibro, Libro


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

    def prestar_libro(self, libro: Libro):
        if libro not in self.libros:
            print(f"✖️ El '{libro.titulo}' no pertenece a la biblioteca")
            return

        if libro.estado == EstadoLibro.PRESTADO:
            print(f"⚠️ El '{libro.titulo}' se encuentra prestado")
            return

        libro.estado = EstadoLibro.PRESTADO
        print(f"👌 Has prestado el '{libro.titulo}' con éxito.")

    def devolver_libro(self, libro: Libro):
        if libro not in self.libros:
            print(f"✖️ El '{libro.titulo}' no pertenece a la biblioteca")
            return

        if libro.estado == EstadoLibro.DISPONIBLE:
            print(f"⚠️ El '{libro.titulo}' ya estaba en la biblioteca")
            return

        libro.estado = EstadoLibro.DISPONIBLE
        print(f"👌 Has devuelto el '{libro.titulo}' a la biblioteca")
