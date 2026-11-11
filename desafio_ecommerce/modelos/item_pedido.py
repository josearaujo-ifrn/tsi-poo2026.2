from modelos.produto import *
from dataclasses import dataclass

class ItemPedido:
    produto: Produto
    quantidade: int

    def subtotal(self) -> float:
        return self.produto.calcular_preco_final() * self.quantidade