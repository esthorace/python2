from typing import Protocol


class PasarelaPago(Protocol):
    def pagar(self, monto: float) -> None:
        pass


class MercadoPagoService:
    def pagar(self, monto: float) -> None:
        # lógica de la API de MP
        print(f"[MercadoPago] procesando pago de ${monto}.")


class PayPalService:
    def pagar(self, monto: float) -> None:
        # lógica de la API de PayPal
        print(f"[PayPal] procesando pago de ${monto}.")


def procesar_pago(pasarela: PasarelaPago, monto: float):
    print("Iniciando transacción...")
    pasarela.pagar(monto)
    print("Fin de transacción.")


pasarela_mp = MercadoPagoService()
pasarela_paypal = PayPalService()

procesar_pago(pasarela_mp, 100)
procesar_pago(pasarela_paypal, 2500)
