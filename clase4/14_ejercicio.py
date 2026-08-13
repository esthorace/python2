"""
Crea una clase Procesador con el atributo nucleos y los métodos iniciar() y detener().
Luego crea una clase Computadora con el atributo marca,
que mediante composición contenga un objeto Procesador,
e implementa los métodos encender() y apagar(),
que primero activen o detengan el procesador y luego muestren el estado de la computadora.
"""


class Procesador:
    def __init__(self, nucleos: int) -> None:
        self.nucleos = nucleos

    def iniciar(self) -> None:
        print(f"Iniciando el procesador con {self.nucleos} nucleos")

    def detener(self) -> None:
        print(f"Deteniendo el procesador con {self.nucleos} nucleos")


class Computadora:
    def __init__(self, marca: str, nucleos: int) -> None:
        self.marca = marca
        self.procesador = Procesador(nucleos)

    def encender(self) -> None:
        self.procesador.iniciar()
        print(f"Encendiendo la computadora {self.marca}")

    def apagar(self) -> None:
        self.procesador.detener()
        print(f"Apagando la computadora {self.marca}")


def main():
    procesador = Procesador(4)
    computadora = Computadora("HP", 4)
    computadora.encender()
    computadora.apagar()


main()
