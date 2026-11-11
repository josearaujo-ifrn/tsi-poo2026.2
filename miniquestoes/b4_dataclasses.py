from dataclasses import dataclass, field
# Exercício 10 - Aula 10: Dataclasses
@dataclass
class Item:
    nome: str
    preco_unitario: float
    quantidade: int

    def calcular_total(self) -> float:
        return self.preco_unitario * self.quantidade

i = Item("Biscoito Globo", 5.50, 3)
print(i)
print(i.calcular_total())