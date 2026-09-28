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
            (f"O salário digitado de {self.nome} é menor que o salário mínimo (R$1600).")
    
    def aumentar(self, percentual: int):
        if percentual > 0 and percentual <= 30:
            self.salario += self.salario * (percentual/100)
        else:
            raise ValueError("O percentual do aumento deve ser entre 0 e 30.")

    def __str__(self):
        return f"Funcionário: {self.nome} - Salário: R${self.salario}"

# Testes/Validações e Questão 8:
try:
    fun01 = Funcionario("João", 1600)
    fun01.aumentar(10)
    print(fun01)
    fun02 = Funcionario("Maria", 1500)
except SalarioInvalidoError as erro_salario:
    print(erro_salario)
except ValueError as erro:
    print(erro)

# Questão 7 - Email

class EmailInvalidoError(Exception):
    pass

class Email:
    def __init__(self, endereco: str):
        self.endereco = endereco

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco: str):
        if "@" not in endereco or "." not in endereco:
            raise EmailInvalidoError(f"O email digitado: '{endereco}' deve conter '@' e '.'")
        else:
            self._endereco = endereco

    def __str__(self):
        return f"O email {self.endereco} é válido."

# Testes/Validações e Questão 8:
try:
    email1 = Email("joao@email.com")
    print(email1)
    email2 = Email("joao@com")
except EmailInvalidoError as erro_email:
    print(erro_email)