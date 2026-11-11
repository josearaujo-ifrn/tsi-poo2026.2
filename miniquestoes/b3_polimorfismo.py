# Exercicio 07 - Aula 07: Polimorfismo
class NotificadorEmail:
    def enviar(self, mensagem: str) -> None:
        print(f"Enviando E-mail: {mensagem}")

class NotificadorSMS:
    def enviar(self, mensagem: str) -> None:
        print(f"Enviando SMS: {mensagem}")

def enviar_alerta(notificador, mensagem: str) -> None:
    notificador.enviar(mensagem)

ne = NotificadorEmail()
ne.enviar("E-mail teste!")
ns = NotificadorSMS()
ns.enviar("SMS teste!")
enviar_alerta(ne, "Alerta teste!")