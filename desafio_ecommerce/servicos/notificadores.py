class NotificadorEmail:
    def enviar(self, destinatario: str, mensagem: str) -> None:
        print(f"[E-MAIL] para {destinatario}: {mensagem}")

class NotificadorSMS:
    def enviar(self, destinatario: str, mensagem: str) -> None:
        print(f"[E-MAIL] para {destinatario}: {mensagem}")