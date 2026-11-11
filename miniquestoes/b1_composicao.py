# Exercício 03 - Aula 03: Composição
class Endereco:
    def __init__(self, rua: str, cidade: str) -> None:
        self.rua = rua
        self.cidade = cidade

    def obter_formatado(self) -> str:
        return f"{self.rua}, {self.cidade}"

class Pessoa:
    def __init__(self, nome: str, rua: str, cidade: str) -> None:
        self.nome = nome
        self.endereco = Endereco(rua, cidade)

    def exibir_dados(self) -> None:
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco.obter_formatado()}")

p = Pessoa("João", "Rua Vinte e Cinco de Março", "São Paulo")
p.exibir_dados()