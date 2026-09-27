## Aula 01 - Exceptions:
--- Exercício 1.1 — Conversor seguro ---
Crie um programa que:
peça ao usuário um número inteiro;
utilize try e except ValueError;
se o valor for válido, imprima o dobro utilizando else;
utilize finally para imprimir "Programa encerrado.".

--- Exercício 1.2 — Divisão protegida ---
Crie um programa que:
peça dois números inteiros;
realize a divisão do primeiro pelo segundo;
trate ZeroDivisionError;
trate ValueError;
utilize else para mostrar o resultado somente quando a divisão for bem-sucedida.

## Aula 02 - Raise:
--- Exercício 2.1 — Validação de idade ---

Crie uma classe Pessoa com:
nome
idade

No __init__, utilize raise ValueError quando a idade for menor que 0.
No programa principal:
crie uma pessoa válida;
tente criar uma pessoa com idade negativa usando try/except.

--- Exercício 2.2 — Conta Bancária ---
Crie uma classe Conta com:
número
saldo protegido (_saldo)

Métodos:
depositar(valor)
sacar(valor)

Regras:
depósito menor ou igual a 0 → raise ValueError
saque maior que o saldo → raise ValueError
No programa principal, demonstre:
um depósito válido;
um saque válido;
um saque inválido tratado com try/except.

## Aula 03 - Exceções Personalizadas e Hierarquias:
--- Exercício 3.1 — Biblioteca ---
Crie uma exceção personalizada chamada LivroEmprestadoError.
Depois, crie uma classe Livro com:
título;
atributo emprestado (booleano).

Método:
- emprestar()
Se o livro já estiver emprestado, lance LivroEmprestadoError.
No programa principal, demonstre o uso com try/except.

--- Exercício 3.2 — Banco ---
Crie uma exceção personalizada chamada SaldoInsuficienteError.
Depois, adapte uma classe Conta para utilizar essa exceção no método sacar().

No programa principal:
faça um depósito;
realize um saque válido;
tente sacar um valor maior que o saldo e trate a exceção específica.

## Aula 04 - Exceções Personalizadas com Integrações:
--- Exercício 4.1 — Biblioteca completa ---

Crie:
Exceção
- LivroEmprestadoError

Classe Livro

Atributos:
título
autor
emprestado

Métodos:
emprestar()
devolver()
__str__

Regras:
Emprestar um livro já emprestado → exceção.
Devolver um livro disponível → exceção.

Programa principal:
Crie 2 livros.
Empreste um.
Tente emprestar novamente.
Devolva o livro.
Imprima o relatório final.

--- Exercício 4.2 — Locadora de Jogos ---
Crie uma exceção personalizada chamada JogoIndisponivelError.

Depois crie uma classe Jogo com:
nome
plataforma
alugado

Métodos:
alugar()
devolver()
__str__
As regras são idênticas às da biblioteca, apenas mudando o contexto.