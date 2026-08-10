class Guitarra:
    def tocar(self):
        print("tin tin tin")


class GuitarraElectrica(Guitarra):
    # def tocar(self):
    #     print("tin tin tin")

    def tocar_con_distorsion(self):
        print("tron tron tron")


guitarra = Guitarra()
guitarra_elec = GuitarraElectrica()
guitarra.tocar()
guitarra_elec.tocar()
guitarra_elec.tocar_con_distorsion()
