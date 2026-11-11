from abc import ABC, abstractmethod
# === Aula 23 - Revisão ===
# item 2

class Animal:
    def __init__(self, nome: str, peso: int):
        self.nome = nome
        self.peso = peso
        self.posicao = 0

    def mover_se(self):
        self.posicao += 1
        print(f"Se moveu! Posição atual: {self.posicao}")

# class Gato(Animal):
#     def __init__(self, nome, peso):
#         pass

# g = Gato("gato", 10)
# g.mover_se()

# item 6

class Veiculo(ABC):
    def __init__(self, placa: str, diaria: int) -> None:
        self.placa = placa
        self.diaria = diaria

    @abstractmethod
    def calcular_aluguel(self, dias: int) -> float:
        """a subclasse vai implementar o calculo de aluguel"""

    def descricao(self) -> str:
        return f"O veículo possui placa {self.placa} com diária R${self.diaria}"

class Carro(Veiculo):
    def __init__(self, placa, diaria) -> None:
        super().__init__(placa, diaria)

    def calcular_aluguel(self, dias: int) -> float:
        return self.diaria * dias

class Moto(Veiculo):
    def __init__(self, placa, diaria) -> None:
        super().__init__(placa, diaria)
    
    def calcular_aluguel(self, dias: int) -> float:
        return self.diaria * dias * 0.8

class Caminhao(Veiculo):
    def __init__(self, placa, diaria) -> None:
        super().__init__(placa, diaria)

    def calcular_aluguel(self, dias):
        return (self.diaria * dias) + 100


# if __name__ == "__main__":
#     c = Carro("XYZ1234", 10)
#     dias = 50
#     c.calcular_aluguel(dias)
#     print(f"{c.descricao()}\nAluguel para {dias} dias: R$ {c.calcular_aluguel(dias)}")

#     c2 = Caminhao("ABC5678", 20)
#     dias = 15
#     c2.calcular_aluguel(dias)
#     print(f"\n{c2.descricao()}\nAluguel para {dias} dias: R$ {c2.calcular_aluguel(dias)}")    

#     m = Moto("IFP2345", 15)
#     dias = 5
#     m.calcular_aluguel(dias)
#     print(f"\n{m.descricao()}\nAluguel para {dias} dias: R$ {m.calcular_aluguel(dias)}")


# item 7
class Locadora:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.lista_veiculos: list[Veiculo] = []

    def cadastrar_veiculo(self, veiculo: Veiculo) -> None:
        self.lista_veiculos.append(veiculo)
        print(f"O veículo com placa {veiculo.placa} foi cadastrado.")

    def faturamento_previsto(self, dias: int) -> float:
        print(f"Faturamento previsto da locadora {self.nome}:")
        return sum(veiculos.calcular_aluguel(dias) for veiculos in self.lista_veiculos)

l = Locadora("loc1")
l.cadastrar_veiculo(Carro("ABC1234", 10))
print(l.faturamento_previsto(10))


# item 8
try:
    v = Veiculo("1A", 10)
except TypeError as erro:
    print(f"[ERRO] TypeError: {erro}")

# item 9

class Prato:
    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco

class Cardapio:
    def __init__(self) -> None:
        self.lista_pratos: list[Prato] = []

    def adicionar_prato(self, prato: Prato) -> None:
        self.lista_pratos.append(prato)
        print(f"Prato {prato.nome} com valor R${prato.preco:.2f} adicionado!")

    def ver_cardapio(self):
        for pratos in self.lista_pratos:
            print(pratos)

class Restaurante:
    def __init__(self, cardapio: Cardapio) -> None:
        self.cardapio = cardapio

p = Prato("Bolo", 10.50)
c = Cardapio()
c.adicionar_prato(p)