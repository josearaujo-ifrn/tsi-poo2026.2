from abc import ABC, abstractmethod
# Desafio Integrador do Bloco 2:
class MetodoPagamento(ABC):
    def __init__(self, valor: float) -> None:
        self.valor = valor

    @abstractmethod
    def processar_pagamento(self) -> bool:
        """As subclasses irão implementar o método."""

class PagamentoCartao(MetodoPagamento):
    def __init__(self, valor: float, numero_cartao: str) -> None:
        super().__init__(valor)
        self.numero_cartao = numero_cartao

    def processar_pagamento(self) -> bool:
        print(f"Pagamento de R${self.valor:.2f} aprovado no cartão {self.numero_cartao}.")
        return True

class PagamentoPix(MetodoPagamento):
    def __init__(self, valor: float, chave_pix: str) -> None:
        super().__init__(valor)
        self.chave_pix = chave_pix

    def processar_pagamento(self) -> None:
        print(f"Pagamento de R${self.valor:.2f} aprovado via PIX {self.chave_pix}.")
        return True

class NotificadorEmail:
    def enviar_notificacao(self, mensagem: str) -> None:
        print(f"[E-MAIL]: {mensagem}")

class NotificadorSMS:
    def enviar_notificacao(self, mensagem: str) -> None:
        print(f"[SMS]: {mensagem}")

class Checkout:
    def __init__(self, notificador) -> None:
        self.notificador = notificador

    def realizar_checkout(self, pagamento: MetodoPagamento) -> None:
        sucesso = pagamento.processar_pagamento()
        if sucesso == True:
            self.notificador.enviar_notificacao(f"Confirmação: Pagamento de R$ {pagamento.valor:.2f} concluído!")
        else:
            print("Pagamento não concluído.")

ne = NotificadorEmail()
ns = NotificadorSMS()
pc = PagamentoCartao(250.0, "1234-5678-9012-3456")
pp = PagamentoPix(80.0, "usuario@pix.com")

c1 = Checkout(ne)
c1.realizar_checkout(pc)
c2 = Checkout(ns)
c2.realizar_checkout(pp)