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