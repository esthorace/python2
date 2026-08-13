"""
# A partir del siguiente código, aplicar la agregación de objetos y no usar composición.

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
"""


class Procesador:
    def __init__(self, nucleos: int) -> None:
        self.nucleos = nucleos

    def iniciar(self) -> None:
        print(f"Iniciando el procesador con {self.nucleos} nucleos")

    def detener(self) -> None:
        print(f"Deteniendo el procesador con {self.nucleos} nucleos")


class Computadora:
    def __init__(self, marca: str, procesador: Procesador) -> None:
        self.marca = marca
        self.procesador = procesador

    def encender(self) -> None:
        self.procesador.iniciar()
        print(f"Encendiendo la computadora {self.marca}")

    def apagar(self) -> None:
        self.procesador.detener()
        print(f"Apagando la computadora {self.marca}")


def main():
    procesador = Procesador(nucleos=4)
    computadora = Computadora(marca="HP", procesador=procesador)
    computadora.encender()
    computadora.apagar()


main()
