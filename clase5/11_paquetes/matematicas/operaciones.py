print(__name__)


def sumar(sumando_a: float, sumando_b: float) -> float:
    return sumando_a + sumando_b


def restar(minuendo: float, sustraendo: float) -> float:
    return minuendo - sustraendo


def multiplicar(multiplicando: float, multiplicador: float) -> float:
    return multiplicando * multiplicador


def dividir(dividendo: float, divisor: float) -> float:
    if divisor == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return dividendo / divisor


if __name__ == "__main__":
    print("********** TEST")
    print(dividir(10, 2))
