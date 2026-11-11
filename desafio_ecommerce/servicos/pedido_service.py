from mixins.notificavel import *
from modelos.item_pedido import *
from excecoes.customizadas import *
from servicos.notificadores import *

class PedidoService(NotificavelMixin):
    def __init__(self, notificador, cliente_email: str) -> None:
        self.notificador = notificador
        self.cliente_email = cliente_email
        self.historico_status: list[str] = []
        self.historico_status.append("Pedido criado!")
        self.itens: list[ItemPedido] = []

    def adicionar_item(self, produto: Produto, quantidade: int) -> None:
        if quantidade <= 0:
            raise EstoqueInsuficienteError("Quantidade inválida para item.")
        else:
            item = ItemPedido(produto, quantidade)
            self.itens.append(item)

    def calcular_total(self) -> float:
        return sum(item.subtotal() for item in self.itens)

    def finalizar_pedido(self, cupom: str = None) -> float:
        total = self.calcular_total()
        if cupom.upper() == "PROMO10":
            total = total * 0.9
        elif cupom.upper() == "INVALIDO":
            raise CupomInvalidoError("Cupom de desconto expirado ou inexistente.")
        self.notificador.enviar(self.cliente_email, ...)
        self.notificar(...)
        self.historico_status.append("Pedido finalizado.")
        return total