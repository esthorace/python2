__all__ = ["area_circulo", "area_rectangulo", "area_triangulo"]

from math import pi


def area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    return pi * radio**2


def area_rectangulo(base, altura):
    """Calcula el área de un rectángulo dado su base y altura."""
    return base * altura


def area_triangulo(base, altura):
    """Calcula el área de un triángulo dado su base y altura."""
    return (base * altura) / 2
