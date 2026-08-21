from time import sleep


def enviar_email_que_tarda_mas(nombre: str):
    print(f"🥲 Enviando email a {nombre}")
    sleep(5)
    print(f"✅ Email enviado a {nombre}")


def enviar_email(nombre: str):
    print(f"Enviando email a {nombre}")
    sleep(2)  # simulando
    print(f"✅ Email enviado a {nombre}")


def main():
    enviar_email_que_tarda_mas("Pepe")
    enviar_email("Juan")
    enviar_email("Luis")


main()
