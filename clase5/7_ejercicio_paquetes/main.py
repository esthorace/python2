from modelos.bibliotecas import Biblioteca
from modelos.libros import Libro


def main():
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


main()
