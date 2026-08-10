class Usuario:
    def __init__(self, nombre: str, contraseña: str) -> None:
        self.nombre = nombre  # atributo público
        self.__contraseña = contraseña  # atributo privado

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Contraseña: {self.__contraseña}"

    def get_contraseña(self) -> str:  # método público
        return self.__contraseña  # devuelve el atributo privado

    def set_contraseña(self, nueva_contraseña: str) -> None:  # método público
        if len(nueva_contraseña) > 4:
            self.__contraseña = (
                nueva_contraseña  # asigna el nuevo valor al atributo privado
            )
        else:
            print("La contraseña debe tener al menos 4 caracteres")


usuario = Usuario("Juan", "123456")
print(usuario)
# print(usuario.__contraseña)  # AttributeError
print(vars(usuario))
# Con los atributos privados no se puede acceder directamente,
# pero se puede acceder a través de los métodos públicos
print(usuario.get_contraseña())
usuario.set_contraseña("xyz123")
print(usuario)
