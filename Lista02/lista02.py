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

# Questão 9 - Conta Bancaria

class ErroDeConta(Exception):
    pass

class ValorInvalidoError(ErroDeConta):
    pass

class SaldoInsuficienteError(ErroDeConta):
    pass

class LimiteExcedidoError(ErroDeConta):
    pass

class ContaBancaria:
    def __init__(self):
        self._saldo = 0.0

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor: int):
        if valor <= 0:
            raise ValorInvalidoError("Depósito inválido: digite apenas números maiores que 0.")
        else:
            self._saldo += valor
            print("Depósito realizado com sucesso.")

    def sacar(self, valor: int):
        if 1 <= valor <= 1000 and self._saldo >= valor:
            self._saldo -= valor
            print("Saque realizado com sucesso.")
        elif valor > 1000:
            raise LimiteExcedidoError\
            ("Limite excedido: limite máximo de saque por operação é R$1000")
        elif valor <= 0:
            raise ValorInvalidoError\
            ("Saque inválido: digite apenas números maiores que 0.")
        else:
            raise SaldoInsuficienteError("Saldo insuficiente.")

try:
    conta1 = ContaBancaria()
    conta1.depositar(1002)
    conta1.sacar(1001)
except LimiteExcedidoError as erro_limite:
    print(erro_limite)
except ValorInvalidoError as erro_valor:
    print(erro_valor)
except SaldoInsuficienteError as erro_saldo:
    print(erro_saldo)