# Aula 01 - Mini Exercicios
class Livro:
    pass

livro01 = Livro()
livro02 = Livro()

print(type(livro01))

# Aula 02 - Mini Exercicios
class Filme:
    def __init__(self, titulo, diretor, ano):
        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano

filme01 = Filme("Gente Grande", "Não sei", 2007)
filme02 = Filme("Gente Grande 2", "Não sei", 2010)

print(filme01.titulo)
print(filme02.diretor)

# Aula 03 - Mini Exercicios
class Lampada:
    def __init__(self):
        self.ligada = False
    def ligar(self):
        self.ligada = True
    def desligar(self):
        self.ligada = False
    def mostrar_estado(self):
        if self.ligada == True:
            print("ligada")
        else:
            print("desligada")

lampada1 = Lampada()

lampada1.mostrar_estado()
lampada1.ligar()
lampada1.mostrar_estado()
lampada1.desligar()
lampada1.mostrar_estado()


# Aula 04 - Mini Exercicios
class ContaBancaria:
    def __init__(self, numero, agencia):
        self.numero = numero
        self.agencia = agencia
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Saque realizado")
        else:
            print("Saldo insuficiente para saque")

    def mostrar_saldo(self):
        print(f"Saldo: {self.saldo}")

conta01 = ContaBancaria("12345", "021")
conta01.depositar(100)
conta01.mostrar_saldo()
conta01.sacar(120)
conta01.sacar(50)
conta01.mostrar_saldo()

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100

    def receber_dano(self, dano):
        self.vida -= dano
        print(f"Recebeu {dano} de dano")

    def curar_vida(self, cura):
        self.vida += cura
        print(f"Recebeu {cura} de cura")

    def status(self):
        print(f"Jogador: {self.nome}, Vida: {self.vida}")

jogador01 = Personagem("Gustavo")
jogador01.receber_dano(10)
jogador01.status()
jogador01.curar_vida(10)
jogador01.status()


# Aula 05 - Mini Exercicios
class ContaBancaria:
    def __init__(self, numero, agencia):
        self.numero = numero
        self.agencia = agencia
        self._saldo = 0

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self,valor):
        if self._saldo >= valor:
            self._saldo -= valor
            print("Saque realizado")
        else:
            print("Saldo insuficiente para saque")

    def mostrar_saldo(self):
        print(f"Saldo: {self._saldo}")

conta01 = ContaBancaria("12345", "021")
conta01.depositar(100)
conta01.mostrar_saldo()
conta01.sacar(101)
conta01.sacar(50)
conta01.mostrar_saldo()

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self._nota = nota

    def atualizar_nota(self, valor):
        self._nota = valor
        print("Nota atualizada!")

    def mostrar_nota(self):
        print(f"Nota: {self._nota}")

    def status(self):
        print(f"Nome: {self.nome} // Nota: {self._nota}")

aluno01 = Aluno("João", 7.5)
aluno01.status()
aluno01.atualizar_nota(8.5)
aluno01.status()

# Aula 06 - Mini Exercicios
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    @property
    def nota(self):
        return self._nota
    
    @nota.setter
    def nota(self, nota: float):
        if nota >= 0 and nota <= 10:
            self._nota = nota
        else:
            print("Somente notas entre 0 e 10.")

    def status(self):
        print(f"Nome: {self.nome} // Nota: {self._nota}")

aluno01 = Aluno("João", 7)
aluno01.status()
aluno01.nota = 8.5
aluno01.status()
aluno01.nota = 11
aluno01.status()

class Retangulo:
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    @property
    def altura(self):
        return self._altura
    
    @property
    def base(self):
        return self._base
    
    @property
    def area(self):
        return self._altura * self._base
    
    @altura.setter
    def altura(self, altura: float):
        if altura > 0:
            self._altura = altura
        else:
            print("Somente números maiores que 0.")
    
    @base.setter
    def base(self, base: float):
        if base > 0:
            self._base = base
        else:
            print("Somente números maiores que 0.")

retangulo01 = Retangulo(10, 5)
print(retangulo01.area)
retangulo02 = Retangulo(0,1)
print(retangulo02.area)

# Aula 07 - Mini Exercicios

class Personagem:
    total_de_personagem = 0
    def __init__(self, nome):
        self.nome = nome
        Personagem.total_de_personagem += 1

    @classmethod
    def quantidade(cls):
        return cls.total_de_personagem

personagem01 = Personagem("Bruno")
print(Personagem.quantidade())
personagem02 = Personagem("Tadeu")
print(Personagem.quantidade())

class Temperatura:
    @staticmethod
    def celsius_para_fahrenheit(c):
        f = (9/5) * c + 32
        return f
    
    @staticmethod
    def fahrenheit_para_celsius(f):
        c = (5/9) * (f - 32)
        return c
    
print(Temperatura.celsius_para_fahrenheit(10))
print(Temperatura.fahrenheit_para_celsius(50))

# Aula 08 - Mini Exercicios

class Livro:

    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.ano})"

livro01 = Livro("Dom Casmurro", "Machado de Assis", 1889)
print(livro01)

class Retangulo:
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    @property
    def altura(self):
        return self._altura
    
    @property
    def base(self):
        return self._base
    
    @property
    def area(self):
        return self._altura * self._base
    
    @altura.setter
    def altura(self, altura: float):
        if altura > 0:
            self._altura = altura
        else:
            print("Somente números maiores que 0.")
    
    @base.setter
    def base(self, base: float):
        if base > 0:
            self._base = base
        else:
            print("Somente números maiores que 0.")

    def __eq__(self, outro):
        if isinstance(outro, Retangulo):
            return self.base == outro.base and self.altura == outro.altura
        else:
            return False

r1 = Retangulo(10, 5)
r2 = Retangulo(10, 5)
r3 = Retangulo(8, 5)

print(r1 == r2)
print(r1 == r3)