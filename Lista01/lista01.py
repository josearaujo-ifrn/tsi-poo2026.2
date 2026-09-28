# Questão 06 - Aluno:
class Aluno:
    def __init__(self, nome: str, matricula: str): # init pra inicializar e atribuir para cada objeto
        self.nome = nome
        self.matricula = matricula
        self.lista_notas = [] # vai criar uma lista de notas para cada aluno

    def lancar_nota(self, valor: float):
        self.lista_notas.append(valor) # append pra adicionar nota na lista de notas

    def media(self):
        total = sum(self.lista_notas) # função sum para somar todas as notas da lista
        media = total/len(self.lista_notas) # total dividido pelo tamanho da lista
        return media
    
    def aprovado(self):
        if self.media() >= 6: # se a média for maior ou igual a 6, será aprovado
            return True
        else:
            return False

    def __str__(self): # imprime o nome, matricula e media
        return f"{self.nome} ({self.matricula}) — média {self.media()}"
    
# Questão 07 - Aluno:
aluno01 = Aluno("Bruno", "20261007")
aluno01.lancar_nota(7)
aluno01.lancar_nota(8)
aluno02 = Aluno("Ana", "20261010")
aluno02.lancar_nota(7.5)
aluno02.lancar_nota(8.5)
aluno03 = Aluno("Gustavo", "20261017")
aluno03.lancar_nota(5)
aluno03.lancar_nota(4.8)
lista_alunos = [aluno01, aluno02, aluno03]
for aluno in lista_alunos: # para cada aluno na lista de alunos
    if aluno.aprovado(): # se aluno for aprovado, imprima o aluno
        print(aluno)

# Questão 08 - Retângulo:
class Retangulo:
    def __init__(self, base, altura): # init pra inicializar e atribuir para cada objeto
        self.base = base
        self.altura = altura 

    def area(self):
        return self.base * self.altura # area de um retangulo é base vezes altura

    def perimetro(self):
        return self.base * 2 + self.altura * 2 # perimetro é soma de todos os lados

    def __eq__(self, outro):
        if isinstance(outro, Retangulo): # se outro objeto for instancia da classe retangulo, verifica se possuem mesmas dimensões
            return self.base == outro.base and self.altura == outro.altura
        else:
            return False

ret1 = Retangulo(5,4)
ret2 = Retangulo(4,5)
print(ret1 == ret2)

# Questão 09 - Data:
class Data:
    def __init__(self, dia: int, mes: int, ano: int): # init pra inicializar e atribuir para cada objeto
        self.dia = dia
        self.mes = mes
        self.ano = ano 

    @classmethod
    def data_string(cls, texto: str): 
        dia, mes, ano = texto.split("/") # separa o dia, mes e ano em uma string usando barra
        return cls(int(dia), int(mes), int(ano)) 

    @staticmethod
    def eh_bissexto(ano: int): # se o ano for divisivel por 4 e não for por 100, ele é bissexto, ou se for divisivel por 400
        return (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0

    def __str__(self):
        return f"{self.dia:02}/{self.mes:02}/{self.ano}" # os numeros entre 1 e 9 não ficam com 0 na esquerda, pra isso se usa {variavel:02}

data01 = Data(20, 9, 2026)
print(data01)