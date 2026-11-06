class Veiculo: 
    def ligar(self): 
        print("Veículo ligado e pronto para rodar!")

class Motorista: 
    def __init__(self, nome: str): 
        self.nome = nome 

    def ligar_veiculo(self, veiculo: Veiculo):
        veiculo.ligar()

c = Veiculo()
m = Motorista("João")
m.ligar_veiculo(c)