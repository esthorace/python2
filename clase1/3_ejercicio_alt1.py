edad = int(input("Edad: "))

if edad >= 18:
    antiguedad = int(input("Antigüedad en el sistema financiero: "))
    ingresos = int(input("Ingreso mensual: "))

    if antiguedad >= 3 and ingresos > 2500 or ingresos >= 4000:
        print("Se aprueba el crédito")
    else:
        print("No se aprueba el crédito")
else:
    print("No se aprueba el crédito")
