class Usuario:
    def __init__(self, nombre: str, contraseña: str) -> None:
        self.nombre = nombre
        self._contraseña = contraseña

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Contraseña: {self._contraseña}"

    # def set_nombre(self, nuevo_valor: str):  # método de instancia
    #     if nuevo_valor:
    #         self.nombre = nuevo_valor
    #     else:
    #         raise ValueError("No puede estar vacío")
    @property
    def contraseña(self) -> str:
        return self._contraseña

    @contraseña.setter
    def contraseña(self, nuevo_valor: str):
        if len(nuevo_valor) > 4:
            self._contraseña = nuevo_valor
        else:
            print("La contraseña debe tener al menos 4 caracteres")


usuario = Usuario("Juan", "123456")
print(usuario)
usuario.contraseña = "abcdef"
print(usuario)
usuario.contraseña = "2"
print(usuario)

# usuario._contraseña = "2"  # aquí hay un problema, ver próximo código
# print(usuario)
