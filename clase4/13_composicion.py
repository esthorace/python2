class Motor:
    def __init__(self, cilindrada: int):
        self.cilindrada = cilindrada

    def arrancar(self):
        print("Motor arrancando...")

    def detener(self):
        print("Motor deteniéndose...")


class Auto:
    def __init__(self, modelo: str, cilindrada: int):
        self.modelo = modelo
        self.motor = Motor(cilindrada)  # composición

    def encender(self):
        self.motor.arrancar()
        print("Auto encendido")

    def apagar(self):
        self.motor.detener()
        print("Auto apagado")


mi_auto = Auto("Ford Mustang", cilindrada=5000)
mi_auto.encender()
mi_auto.apagar()
