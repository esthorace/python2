class Vehiculo:
    def andar(self):
        print("El vehículo está en movimiento")


class Auto(Vehiculo):
    def tocar_bocina(self):
        print("El auto está tocando bocina")


class MovimientosMarinosMixin:
    def virar_babor(self):
        print("Virando a babor")

    def virar_estribor(self):
        print("Virando a estribor")


class Lancha(Vehiculo, MovimientosMarinosMixin):
    pass


auto = Auto()
auto.andar()
auto.tocar_bocina()
print()
lancha = Lancha()
lancha.andar()
lancha.virar_babor()
lancha.virar_estribor()
