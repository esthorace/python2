class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"Usuario: {self.nombre} {self.apellido}"


def main():
    usuario = Usuario("Juan", "Perez")
    print(usuario)


main()
