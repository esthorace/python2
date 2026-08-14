from typing import Protocol


class MascotaHabladora(Protocol):
    def hablar(self) -> None:
        pass


class Gato:
    def hablar(self):
        print("miau")


class Perro:
    def hablar(self):
        print("guau")


class Loro:
    def hablar(self):
        print("hola!")


def escuchar_mascota(animal: MascotaHabladora):
    animal.hablar()


gato = Gato()
perro = Perro()
loro = Loro()

escuchar_mascota(gato)
escuchar_mascota(perro)
escuchar_mascota(loro)
