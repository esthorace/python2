def es_mayor_de_edad(edad):
    return edad >= 18

def solicitar_datos():
    edad = int(input("Edad: "))
    antiguedad = None
    ingresos = None
    if es_mayor_de_edad(edad):
        antiguedad = int(input("Antigüedad en el sistema financiero: "))
        ingresos = int(input("Ingreso mensual: "))
    return edad, antiguedad, ingresos


def es_perfil_estandar(antiguedad, ingresos):
    return antiguedad >= 3 and ingresos > 2500


def es_perfil_premium(ingresos):
    return ingresos >= 4000


def evaluar_credito(edad, antiguedad, ingresos):
    if not es_mayor_de_edad(edad):
        return False

    perfiles = [
        es_perfil_estandar(antiguedad, ingresos),
        es_perfil_premium(ingresos),
    ]
    return any(perfiles)


def main():
    edad, antiguedad, ingresos = solicitar_datos()
    aprobado = evaluar_credito(edad, antiguedad, ingresos)

    if aprobado:
        print("Se aprueba el crédito")
    else:
        print("No se aprueba el crédito")


main()
