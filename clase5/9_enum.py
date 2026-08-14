from enum import Enum


class EstadoPedido(str, Enum):
    PENDIENTE = "pendiente"
    ENVIADO = "enviado"
    ENTREGADO = "entregado"


estado_actual = EstadoPedido.PENDIENTE

if estado_actual == EstadoPedido.PENDIENTE:
    print("El paquete está pendiente de ser enviado")
