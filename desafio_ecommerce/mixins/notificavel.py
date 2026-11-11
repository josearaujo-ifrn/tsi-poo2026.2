class NotificavelMixin:
    def notificar(self, mensagem: str) -> None:
        print(f"[NOTIFICAÇÃO SISTEMA]: {mensagem}")