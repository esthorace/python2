class Usuario:
    sistema: str = "Django"

    def __init__(self, username: str) -> None:
        self.username = username

    @classmethod
    def cambiar_sistema(cls, nuevo_valor: str):
        cls.sistema = nuevo_valor


admin = Usuario(username="admin")
user = Usuario(username="user")

print(admin.sistema)
print(user.sistema)

Usuario.cambiar_sistema("FastAPI")
print()
print(admin.sistema)
print(user.sistema)

print(vars(user))
print(vars(admin))
