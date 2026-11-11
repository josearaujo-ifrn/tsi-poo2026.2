# Exercicio 05 - Aula 05: Herança
class Veiculo:
    def __init__(self, marca: str, modelo: str) -> None:
        self.marca = marca
        self.modelo = modelo

    def acelerar(self) -> None:
        print("Veículo acelerando...")

class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, qtd_portas: int) -> None:
        super().__init__(marca, modelo)
        self.qtd_portas = qtd_portas

    def acelerar(self) -> None:
        print(f"Carro {self.marca} {self.modelo} acelerando com {self.qtd_portas} portas!")

class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str) -> None:
        super().__init__(marca, modelo)

    def acelerar(self) -> None:
        print(f"Moto {self.marca} {self.modelo} acelerando!")

c = Carro("XYZ", "Hibrido", 6)
c.acelerar()
m = Moto("XYZ", "Veloz")
m.acelerar()