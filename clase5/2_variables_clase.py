class Usuario:
    sistema: str = "Django"  # variable de clase

    def __init__(self, username: str) -> None:
        self.username = username  # variable de instancia


admin = Usuario(username="admin")
user = Usuario(username="user")

print(admin.sistema)
print(user.sistema)

# admin.sistema = "FastAPI"  # 🚨 Esto crea una variable de instancia, no cambia la variable de clase
Usuario.sistema = "FastAPI"
print()
print(admin.sistema)
print(user.sistema)

print(vars(user))
print(vars(admin))
