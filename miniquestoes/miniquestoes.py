# Exercício 01 - Aula 01: Associação
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

# Exercício 02 - Aula 02: Agregação
class Livro:
    def __init__(self, titulo: str, autor: str) -> None:
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.livros: list[Livro] = []
    
    def adicionar_livro(self, livro: Livro) -> None:
        self.livros.append(livro)
    
    def exibir_livro(self) -> None:
        for livro in self.livros:
             print(f"Título: {livro.titulo} -- Autor: {livro.autor}")

li = Livro("Dom Casmurro", "Machado de Assis")
li2 = Livro("Memórias Póstumas", "Machado de Assis")
bi = Biblioteca("Biblioteca")
bi.adicionar_livro(li)
bi.adicionar_livro(li2)
bi.exibir_livro()

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