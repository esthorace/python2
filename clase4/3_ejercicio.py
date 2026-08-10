"""
Crear un método de instancia para establecer una contraseña
class Usuario:
    def __init__(self, nombre: str, contraseña: str) -> None:
        self.nombre = nombre
        self.contraseña = contraseña

    def __str__(self) -> str:
        return self.nombre

    def set_nombre(self, nuevo_valor: str):  # método de instancia
        if nuevo_valor:
            self.nombre = nuevo_valor
        else:
            raise ValueError("No puede estar vacío")


def main():
    usuario_1 = Usuario("admin", "123")
    usuario_2 = Usuario("juan", "789")
    usuario_3 = Usuario("pepe", "555")
    usuarios = (usuario_1, usuario_2, usuario_3)
    for usuario in usuarios:
        print(usuario, end=" ")
    print()
    usuario_1.set_nombre("superadmin")
    for usuario in usuarios:
        print(usuario, end=" ")


main()
"""


class Usuario:
    def __init__(self, nombre: str, contraseña: str) -> None:
        self.nombre = nombre
        self.contraseña = contraseña

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Contraseña: {self.contraseña}"

    def set_nombre(self, nuevo_valor: str):  # método de instancia
        if nuevo_valor:
            self.nombre = nuevo_valor
        else:
            raise ValueError("No puede estar vacío")

    def set_contraseña(self, nuevo_valor: str):
        if len(nuevo_valor) > 4:
            self.contraseña = nuevo_valor
        else:
            print("La contraseña debe tener al menos 4 caracteres")


def main():
    usuario_1 = Usuario("admin", "123")
    usuario_2 = Usuario("juan", "789")
    usuario_3 = Usuario("pepe", "555")
    usuarios = (usuario_1, usuario_2, usuario_3)
    for usuario in usuarios:
        print(usuario, end=" ")
    print()
    usuario_1.set_nombre("superadmin")
    usuario_1.set_contraseña("1")
    # usuario_1.contraseña = "1"
    for usuario in usuarios:
        print(usuario, end=" ")


main()
