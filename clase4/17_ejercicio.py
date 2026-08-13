"""
Crear un programa que tenga dos modelos: Biblioteca y Libro.

Atributos de Libro: titulo, autor, año
Atributos de Biblioteca: nombre, libros (lista de instancias de Libro)
Métodos de Biblioteca: agregar(libro: Libro), eliminar, listar

- Crear 3 libros, agregarlos a la biblioteca y listarlos

libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943)
libro2 = Libro("1984", "George Orwell", 1949)
libro3 = Libro("Órganon", "Aristóteles", -384)
"""


# class Libro:
#     def __init__(self, titulo: str, autor: str, año: int) -> None:
#         self.titulo = titulo
#         self.autor = autor
#         self.año = año

from dataclasses import dataclass


@dataclass
class Libro:
    titulo: str
    autor: str
    año: int


libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943)
libro2 = Libro("1984", "George Orwell", 1949)
libro3 = Libro("Órganon", "Aristóteles", -384)

print(libro1)
print(libro2)
print(libro3)
