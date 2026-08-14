import matematicas

print(__name__)
if __name__ == "__main__":
    resultado_suma = matematicas.sumar(5, 4)
    resultado_resta = matematicas.restar(10, 2)
    resultado_area_rectangulo = matematicas.area_rectangulo(10, 5)
    resultado_area_circulo = matematicas.area_circulo(10)

    print(f"Suma: {resultado_suma}")
    print(f"Resta: {resultado_resta}")
    print(f"Área del rectángulo: {resultado_area_rectangulo}")
    print(f"Área del círculo: {resultado_area_circulo}")
    # print(matematicas.pi)  # lo desconoce porque en calculo_areas no lo puse en __all__
