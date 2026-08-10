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
        return "********" + self.__contraseña

    @property
    def contraseña_inversa(self) -> str:
        return self.__contraseña[::-1]


def main():
    usuario = Usuario("Juan", "123456")
    print(usuario)
    usuario.contraseña = input("Ingrese la nueva contraseña: ")
    print(usuario)
    print(usuario.contraseña)
    print(usuario.contraseña_inversa)


main()
