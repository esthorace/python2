class Guitarra:
    def __init__(self):
        self.soy_instrumento = True

    def tocar(self):
        print("tin tin tin")


class GuitarraElectrica(Guitarra):
    def tocar_con_distorsion(self):
        print("tron tron tron")


guitarra = Guitarra()
guitarra.tocar()
print(guitarra.soy_instrumento)

print()
guitarra_elec = GuitarraElectrica()
guitarra_elec.tocar()
guitarra_elec.tocar_con_distorsion()
print(guitarra_elec.soy_instrumento)
