# # Exercício 01 - Aula 01: Associação
# class Veiculo: 
#     def ligar(self): 
#         print("Veículo ligado e pronto para rodar!")

# class Motorista: 
#     def __init__(self, nome: str): 
#         self.nome = nome 

#     def ligar_veiculo(self, veiculo: Veiculo):
#         veiculo.ligar()

# c = Veiculo()
# m = Motorista("João")
# m.ligar_veiculo(c)

# # Exercício 02 - Aula 02: Agregação
# class Livro:
#     def __init__(self, titulo: str, autor: str) -> None:
#         self.titulo = titulo
#         self.autor = autor

# class Biblioteca:
#     def __init__(self, nome: str) -> None:
#         self.nome = nome
#         self.livros: list[Livro] = []
    
#     def adicionar_livro(self, livro: Livro) -> None:
#         self.livros.append(livro)
    
#     def exibir_livro(self) -> None:
#         for livro in self.livros:
#              print(f"Título: {livro.titulo} -- Autor: {livro.autor}")

# li = Livro("Dom Casmurro", "Machado de Assis")
# li2 = Livro("Memórias Póstumas", "Machado de Assis")
# bi = Biblioteca("Biblioteca")
# bi.adicionar_livro(li)
# bi.adicionar_livro(li2)
# bi.exibir_livro()

# # Exercício 03 - Aula 03: Composição
# class Endereco:
#     def __init__(self, rua: str, cidade: str) -> None:
#         self.rua = rua
#         self.cidade = cidade

#     def obter_formatado(self) -> str:
#         return f"{self.rua}, {self.cidade}"

# class Pessoa:
#     def __init__(self, nome: str, rua: str, cidade: str) -> None:
#         self.nome = nome
#         self.endereco = Endereco(rua, cidade)

#     def exibir_dados(self) -> None:
#         print(f"Nome: {self.nome}")
#         print(f"Endereço: {self.endereco.obter_formatado()}")

# p = Pessoa("João", "Rua Vinte e Cinco de Março", "São Paulo")
# p.exibir_dados()

# Exercício 04 - Aula 04: Associação, Agregação e Composição
class Projetor:
    def __init__(self, nome_aula: str) -> None:
        self.nome_aula = nome_aula

    def exibir_slides(self) -> None:
        print(f"Exibindo slides da aula de {self.nome_aula}...")

class Professor:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def dar_aula(self, projetor: Projetor) -> None:
        projetor.exibir_slides()

class GradeCurricular:
    def __init__(self, nome_curso: str) -> None:
        self.nome_curso = nome_curso

    def detalhar(self) -> None:
        print(f"Nome do curso: {self.nome_curso}")

class Universidade:
    def __init__(self, nome: str, grade_curricular: str):
        self.nome = nome
        self.grade_curricular = GradeCurricular(grade_curricular)
        self.lista_professor: list[Professor] = []
    
    def contratar_professor(self, professor: Professor) -> None:
        self.lista_professor.append(professor)
        print(f"O professor {professor.nome} foi contratado.")

    def exibir_relatorio(self) -> None:
        print("=== Relatório da Universidade ===")
        print(f"Nome da Universidade: {self.nome}")
        print(f"Grade Curricular: {self.grade_curricular.nome_curso}")
        for professor in self.lista_professor:
            print(professor.nome)

p1 = Projetor("Programação Orientada a Objetos")
p1.exibir_slides()
p2 = Professor("Higor")
g = GradeCurricular("Sistemas para Internet")
u = Universidade("Universidade Federal Fluminense", "Sistemas para Internet")
u.contratar_professor(p2)
u.exibir_relatorio()