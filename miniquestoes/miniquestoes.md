### Exercício 1.2 — Complete o Código 
Monte o método `dirigir` na classe `Motorista` de modo que ele receba um objeto `Veiculo` como parâmetro e chame seu método `ligar()`:
class Veiculo:
    def ligar(self):
        print("Veículo ligado e pronto para rodar!")

class Motorista:
    def __init__(self, nome: str):
        self.nome = nome

    # Escreva aqui o método dirigir que recebe o veículo por parâmetro

### **Exercício 2.2 — Complete o Código** 
Monte a classe `Biblioteca` que agrega objetos da classe `Livro` em uma lista e possui um método para listar todos os livros cadastrados:
class Livro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self, nome: str):
        self.nome = nome
        # 1. Crie a lista vazia para armazenar os livros

    def adicionar_livro(self, livro: Livro):
        # 2. Adicione o livro na lista interna

    def exibir_livros(self):
        # 3. Imprima o título e o autor de cada livro agregado
        pass
# Teste seu código instanciando 2 livros e adicionando à biblioteca!

### **Exercício 3.2 — Complete o Código** 
Implemente o relacionamento de **Composição** entre a classe `Pessoa` e a classe `Endereco`. Ao instanciar uma `Pessoa`, ela deve criar internamente o seu próprio objeto `Endereco` com a rua e a cidade fornecidas:

class Endereco:
    def __init__(self, rua: str, cidade: str) -> None:
        self.rua = rua
        self.cidade = cidade

    def obter_formatado(self) -> str:
        return f"{self.rua}, {self.cidade}"

class Pessoa:
    def __init__(self, nome: str, rua: str, cidade: str) -> None:
        self.nome = nome
        # 1. Crie o objeto Endereco DENTRO do __init__ (Composição)

    def exibir_dados(self) ->; None:
        # 2. Imprima o nome e o endereço formatado chamando o método do Endereco interno
        pass

# Teste seu código instanciando apenas uma Pessoa (sem instanciar Endereco fora):
# p = Pessoa("Carlos", "Av. Paulista", "São Paulo")
# p.exibir_dados()