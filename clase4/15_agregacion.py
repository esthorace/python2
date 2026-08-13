class Motor:
    def __init__(self, cilindrada: int):
        self.cilindrada = cilindrada

    def arrancar(self):
        print(f"Motor de {self.cilindrada} cilindradas arrancando...")

    def detener(self):
        print(f"Motor de {self.cilindrada} cilindradas deteniéndose...")


class Auto:
    def __init__(self, modelo: str, motor: Motor):
        self.modelo = modelo
        self.motor = motor  # agregación

    def encender(self):
        self.motor.arrancar()
        print("Auto encendido")

    def apagar(self):
        self.motor.detener()
        print("Auto apagado")


motor = Motor(cilindrada=5000)
motor2 = Motor(cilindrada=10000)
mi_auto = Auto("Ford Mustang", motor)
mi_auto.encender()
mi_auto.apagar()
mi_auto = Auto("Lamborghini Aventador", motor2)
mi_auto.encender()
mi_auto.apagar()
