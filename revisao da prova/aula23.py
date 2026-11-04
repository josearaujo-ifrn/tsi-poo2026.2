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


if __name__ == "__main__":
    c = Carro("XYZ1234", 10)
    dias = 50
    c.calcular_aluguel(dias)
    print(f"{c.descricao()}\nAluguel para {dias} dias: R$ {c.calcular_aluguel(dias)}")

    c2 = Caminhao("ABC5678", 20)
    dias = 15
    c2.calcular_aluguel(dias)
    print(f"\n{c2.descricao()}\nAluguel para {dias} dias: R$ {c2.calcular_aluguel(dias)}")    

    m = Moto("IFP2345", 15)
    dias = 5
    m.calcular_aluguel(dias)
    print(f"\n{m.descricao()}\nAluguel para {dias} dias: R$ {m.calcular_aluguel(dias)}")