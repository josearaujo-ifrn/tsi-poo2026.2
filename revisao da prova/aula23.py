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
# falta corrigir
# class Locadora:
#     def __init__(self, nome: str) -> None:
#         self.nome = nome

#     def cadastrar_veiculo(self, veiculo: Veiculo) -> str:
#         print(f"O veículo {veiculo} foi cadastrado.")

#     def faturamento_previsto(self, dias: int) -> int:
#         return Veiculo.calcular_aluguel(dias)

# l = Locadora("loc1")
# l.cadastrar_veiculo(Carro("ABC1234", 10))
# l.faturamento_previsto(10)

# item 9

class Prato:
    def __init__(self, nome: str, preco: int):
        self.nome = nome
        self.preco = preco
        # falta coisa
    
class Cardapio:
    def __init__(self):
        pass

    def listar_pratos(self, pratos: Prato):
        self.lista_pratos += [pratos]
        # falta coisa

class Restaurante:
    def __init__(self, nome: str):
        self.nome = nome

    def ver_cardapio(self, cardapio: Cardapio):
        for pratos in cardapio: # falta coisa
            print(pratos)