from dataclasses import dataclass
from enum import Enum


class EstadoLibro(str, Enum):
    DISPONIBLE = "En biblioteca"
    PRESTADO = "Prestado"


@dataclass
class Libro:
    titulo: str
    autor: str
    año: int
    estado: EstadoLibro = EstadoLibro.DISPONIBLE
