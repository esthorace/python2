from typing import Any


def validar_entero(valor: Any) -> bool:
    if isinstance(valor, bool):
        return False

    if isinstance(valor, str):
        if valor.startswith(("+", "-")):
            return valor[1:].isdigit()
        return valor.isdigit()

    return isinstance(valor, int)
