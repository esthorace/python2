class User:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def login(self) -> None:
        print(f"Bienvenido {self.username}")

    def despedirse(self):
        print("👋")


class Staff(User):
    def login(self) -> None:
        print("-- PORTAL DEL PROFESIONAL ---")
        super().login()


class Patient(User):
    def login(self) -> None:
        print("-- PORTAL DEL PACIENTE ---")
        super().login()
        self.despedirse()


user = User("usuario", "")
user.login()
staff = Staff("Dr. House", "1234")
staff.login()
patient = Patient("Tere", "456")
patient.login()
