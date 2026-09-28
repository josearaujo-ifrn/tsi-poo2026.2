# Questão 6 - Funcionário

class SalarioInvalidoError(Exception):
    pass
class Funcionario:
    def __init__(self, nome: str, salario: int):
        self.salario_minimo = 1600
        self.nome = nome
        self.salario = salario

    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, salario):
        if salario >= self.salario_minimo:
            self._salario = salario
        else:
            raise SalarioInvalidoError\
            ("O salário digitado é menor que o salário mínimo (R$1600).")
    
    def aumentar(self, percentual: int):
        if percentual > 0 and percentual <= 30:
            self.salario += self.salario * (percentual/100)
        else:
            raise ValueError("O percentual do aumento deve ser entre 0 e 30.")

    def __str__(self):
        return f"Funcionário: {self.nome} - Salário: R${self.salario}"

try:
    fun01 = Funcionario("João", 1600)
    fun01.aumentar(10)
    print(fun01)
except SalarioInvalidoError as erro_salario:
    print(erro_salario)
except ValueError as erro:
    print(erro)