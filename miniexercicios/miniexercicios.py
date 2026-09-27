# # Questão 1.1
# try:
#     numero = int(input("Digite um número: "))
# except ValueError:
#     print("Erro: digite somente números.")
# else:
#     print(f"Dobro do número: {numero * 2}")
# finally:
#     print("Programa encerrado.")

# # Questão 1.2
# try:
#     numero1 = int(input("Digite o primeiro número: "))
#     numero2 = int(input("Digite o segundo número: "))
#     divisao_numeros = numero1/numero2
# except ZeroDivisionError:
#     print("Não se divide por 0.")
# except ValueError:
#     print("Digite somente números.")
# else:
#     print(f"Resultado: {divisao_numeros}")

# # Questão 2.1
# class Pessoa:
#     def __init__(self, nome: str, idade: int):
#         self.nome = nome
#         self.idade = idade
#         if idade < 0:
#             raise ValueError("Digite apenas números maiores que 1")

# pessoa1 = Pessoa("Breno", 25)

# try:
#     pessoa2 = Pessoa("João", -1)
# except ValueError:
#     print("Somente idades maiores que 1.")

# # Questão 2.2
# class ContaBancaria:
#     def __init__(self, numero: str):
#         self.numero = numero
#         self._saldo = 0.0
    
#     def depositar(self, valor: int):
#         if valor <= 0:
#             raise ValueError("Depósito inválido.")
#         else:
#             self._saldo += valor
    
#     def sacar(self, valor: int):
#         if valor > self._saldo:
#             raise ValueError("Saque maior que o saldo.")
#         else:
#             self._saldo -= valor
# try:
#     conta1 = ContaBancaria("02122-3")
#     conta1.depositar(-1)
#     conta1.sacar(1)
# except ValueError as erro:
#     print(erro)

# try:
#     conta2 = ContaBancaria("02221-3")
#     conta2.sacar(1)
# except ValueError as erro:
#     print(erro)

# # Questão 3.1
# class LivroEmprestadoError(Exception):
#     pass

# class Livro:
#     def __init__(self, titulo: str):
#         self.titulo = titulo
#         self.emprestado = False

#     def emprestar_livro(self):
#         if self.emprestado == True:
#             raise LivroEmprestadoError(f"O livro {self.titulo} está emprestado.")
#         else:
#             self.emprestado = True
#             print(f"O livro '{self.titulo}' agora está emprestado.")
# try:
#     livro1 = Livro("A Moreninha")
#     livro1.emprestar_livro()
#     livro1.emprestar_livro()
# except LivroEmprestadoError as erro:
#     print(erro)

# class SaldoInsuficienteError(Exception):
#     pass

# class Conta:
#     def __init__(self, numero: str):
#         self.numero = numero
#         self._saldo = 0.0
    
#     def depositar(self, valor: int):
#         if valor <= 0:
#             raise ValueError("Depósito inválido.")
#         else:
#             self._saldo += valor
    
#     def sacar(self, valor: int):
#         if valor > self._saldo:
#             raise SaldoInsuficienteError("Saque maior que o saldo.")
#         else:
#             self._saldo -= valor
# try:
#     conta3 = Conta("01121-1")
#     conta3.depositar(100)
#     conta3.sacar(101)
# except SaldoInsuficienteError as erro:
#     print(erro)

# Questão 4.1
class LivroEmprestadoError(Exception):
    pass

class Livro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor
        self.emprestado = False

    def emprestar_livro(self):
        if self.emprestado == True:
            raise LivroEmprestadoError(f"O livro {self.titulo} está emprestado.")
        else:
            self.emprestado = True
            print(f"O livro '{self.titulo}' agora está emprestado.")

    def devolver_livro(self):
        if self.emprestado == True:
            self.emprestado = False
            print(f"O livro {self.titulo} foi devolvido.")
        else:
            raise LivroEmprestadoError(f"O livro não foi pego.")
    
    def __str__(self):
        if self.emprestado == True:
            self.emprestado = "Indisponível"
        else:
            self.emprestado = "Disponível"
        return f"Livro: {self.titulo}\nAutor: {self.autor}\nStatus: {self.emprestado}"
try:
    livro1 = Livro("A Moreninha", "Joaquim Manuel")
    livro2 = Livro("Dom Casmurro", "Machado de Assis")
    livro1.emprestar_livro()
    livro1.emprestar_livro()
    livro1.devolver_livro()
except LivroEmprestadoError as erro:
    print(erro)

print(livro1)

# Questão 4.2

class JogoIndisponivelError(Exception):
    pass

class Jogo:
    def __init__(self, nome: str, plataforma: str):
        self.nome = nome
        self.plataforma = plataforma
        self.alugado = False
    
    def alugar_jogo(self):
        if self.alugado == False:
            self.alugado = True
            print(f"O jogo {self.nome} foi alugado.")
        else:
            raise JogoIndisponivelError(f"O jogo {self.nome} ja está alugado.")

    def devolver_jogo(self):
        if self.alugado == True:
            self.alugado = False
            print(f"O jogo {self.nome} foi devolvido.")
        else:
            print(f"O jogo {self.nome} não foi alugado.")
    
    def __str__(self):
        if self.alugado == True:
            self.alugado = "Indisponível"
        else:
            self.alugado = "Disponível"
        return f"Jogo: {self.nome}\nPlataforma: {self.plataforma}\nStatus: {self.alugado}"

try:
    jogo1 = Jogo("Jogo tal", "Computador")
    jogo1.alugar_jogo()
except JogoIndisponivelError as erro:
    print(erro)

print(jogo1)