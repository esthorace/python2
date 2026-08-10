"""
# Crear properties para el atributo nombre (getter y setter)

class Usuario:
    def __init__(self, nombre: str, contraseña: str) -> None:
        self.nombre = nombre
        self.__contraseña = contraseña

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Contraseña: {self.__contraseña}"

    @property
    def contraseña(self) -> str:
        return f"{self.__contraseña}"

    @contraseña.setter
    def contraseña(self, nueva_contraseña: str) -> None:
        if len(nueva_contraseña) > 4:
            self.__contraseña = nueva_contraseña
        else:
            print("La contraseña debe tener al menos 4 caracteres")

    @contraseña.getter
    def contraseña(self) -> str:
        return self.__contraseña


def main():
    usuario = Usuario("Juan", "123456")
    usuario.contraseña = input("Ingrese la nueva contraseña: ")
    print(usuario.contraseña)


main()
"""


class Usuario:
    def __init__(self, nombre: str, contraseña: str) -> None:
        self.__nombre = nombre
        self.__contraseña = contraseña

    def __str__(self) -> str:
        return f"Nombre: {self.__nombre}, Contraseña: {self.__contraseña}"

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.getter
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        if len(nuevo_nombre) > 4:
            self.__nombre = nuevo_nombre
        else:
            print("El nombre debe tener al menos 4 caracteres")

    @property
    def contraseña(self) -> str:
        return f"{self.__contraseña}"

    @contraseña.getter
    def contraseña(self) -> str:
        return self.__contraseña

    @contraseña.setter
    def contraseña(self, nueva_contraseña: str) -> None:
        if len(nueva_contraseña) > 4:
            self.__contraseña = nueva_contraseña
        else:
            print("La contraseña debe tener al menos 4 caracteres")


def main():
    usuario = Usuario("Juan", "123456")
    usuario.nombre = input("Ingrese el nuevo nombre: ")
    print(usuario.nombre)
    usuario.contraseña = input("Ingrese la nueva contraseña: ")
    print(usuario.contraseña)


main()
