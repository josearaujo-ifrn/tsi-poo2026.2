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