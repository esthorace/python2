class Gato:
    def hablar(self):
        print("miau")


class Perro:
    def hablar(self):
        print("guau")


def escuchar_mascota(animal):
    animal.hablar()


gato = Gato()
perro = Perro()

escuchar_mascota(gato)
escuchar_mascota(perro)
