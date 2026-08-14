from gestion_tienda.productos import Producto


def main():
    celular = Producto("Celular", 1000.0)
    teclado = Producto("Teclado", 50.0)
    print(Producto.cantidad_total)
    print(celular.calcular_precio_final())
    print(teclado.calcular_precio_final())

    celular.aplicar_descuento(porcentaje=10)
    print(celular.calcular_precio_final())


main()
