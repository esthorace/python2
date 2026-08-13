"""
from dataclasses import dataclass

3 modelos:

Ciudad (nombre, poblacion)
Persona (nombre, edad, ciudad_de_origen)
TarjetaCredito (titular, numero, vencimiento, codigo)

"""

from dataclasses import dataclass


@dataclass
class Ciudad:
    nombre: str
    poblacion: int


@dataclass
class Persona:
    nombre: str
    edad: int
    ciudad_de_origen: str


@dataclass
class TarjetaCredito:
    titular: str
    numero: str
    vencimiento: str
    codigo: str
