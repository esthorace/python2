class Producto:
    porcentaje_iva = 0.21
    cantidad_total = 0

    def __init__(self, nombre: str, precio_base: float) -> None:
        self.nombre = nombre
        self.precio_base = precio_base
        Producto.cantidad_total += 1

    def calcular_precio_final(self):
        return self.precio_base * (1 + Producto.porcentaje_iva)

    def aplicar_descuento(self, porcentaje: float):
        self.precio_base -= self.precio_base * (porcentaje / 100)
