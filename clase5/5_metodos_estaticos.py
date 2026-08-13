class Usuario:
    sistema: str = "Django"

    def __init__(self, username: str) -> None:
        self.username = username

    @classmethod
    def cambiar_sistema(cls, nuevo_valor: str):
        cls.sistema = nuevo_valor

    @staticmethod
    def info():
        print("Hola, esta es una clase para manejar el registro de usuario")


admin = Usuario(username="admin")
Usuario.info()
