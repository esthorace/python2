"""
A partir del siguiente código, crear un método para cambiar el nombre:

class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}"
"""


class Usuario:
    def __init__(self, nombre: str, apellido: str):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}"

    def set_nombre(self, nuevo_valor: str):
        if nuevo_valor:
            self.nombre = nuevo_valor


def main():
    usuario1 = Usuario("Juan", "Perez")
    usuario2 = Usuario("Maria", "Gomez")
    usuario3 = Usuario("Pedro", "Gomez")
    usuarios = [usuario1, usuario2, usuario3]
    for usuario in usuarios:
        print(usuario)

    usuario1.set_nombre("Juan Pablo")

    for usuario in usuarios:
        print(usuario)


main()
