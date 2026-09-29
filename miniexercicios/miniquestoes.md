### Questões criadas pelo ChatGPT para me ajudar nos assuntos
## Exercício 1 — Aula 1 (Classes e Instâncias)
Crie uma classe chamada Livro.
Ela pode ficar vazia (pass).

Depois:
Crie duas instâncias chamadas livro1 e livro2.
Imprima o tipo de livro1 usando type().
Objetivo: entender a criação de instâncias.

## Exercício 2 — Aula 2 (Atributos e __init__)
Crie uma classe Filme com os atributos:
titulo
diretor
ano

Depois:
Crie dois filmes diferentes.
Imprima o título do primeiro.
Imprima o diretor do segundo.
Objetivo: praticar atributos e construtor.

## Exercício 3 — Aula 3 (Métodos de Instância)
Crie uma classe Lampada.
Atributos
- ligada (começa como False)

Métodos
ligar() → muda para True
desligar() → muda para False
mostrar_estado() → imprime "Ligada" ou "Desligada"

## Exercício 4.1 — Conta Bancária
Crie a classe ContaBancaria com exatamente estes atributos:
numero
agencia
saldo (inicia em 0)

Implemente os métodos:
depositar(valor)
sacar(valor) → retorna True ou False
mostrar_saldo() → imprime o saldo atual

## Exercício 4.2 — Personagem de Jogo (mais divertido 🎮)
Crie uma classe Personagem.
Atributos:
nome
vida (começa com 100)

Métodos:
receber_dano(valor) → diminui a vida
curar(valor) → aumenta a vida
status() → imprime nome e vida

## Exercício 5.1 — Conta Bancária Encapsulada

Reescreva sua ContaBancaria fazendo apenas uma alteração:
Troque self.saldo por self._saldo
Depois adapte todos os métodos para continuarem funcionando.

Teste:
Depositar 200
Sacar 50
Mostrar saldo

Objetivo: acostumar-se com a convenção do atributo protegido.

## Exercício 5.2 — Cadastro de Aluno
Crie uma classe Aluno.
Atributos:
nome (público)
_nota (protegido)

Métodos:
atualizar_nota(valor) → altera _nota
mostrar_nota() → imprime a nota
status() → imprime nome e nota

## Exercício 6.1 — Aluno com Property
Refatore sua classe Aluno.

Requisitos:
nome permanece público.
_nota continua sendo o atributo interno.

Crie uma property chamada nota.
A nota deve aceitar apenas valores entre 0 e 10.

## Exercício 6.2 — Retângulo
Crie uma classe Retangulo.
Atributos:
base
altura

Properties:
base → deve aceitar apenas valores maiores que 0.
altura → mesma regra.
area → somente leitura, calculada automaticamente.

## Exercício 7.1 — Contador de Personagens
Crie uma classe Personagem.
Requisitos:
Atributo de classe:
- total_personagens = 0

Atributos de instância:
- nome

Construtor:
Sempre que um personagem for criado, aumente o contador.

Class Method:
Crie um método chamado quantidade() que retorne o total de personagens.

## Exercício 7.2 — Calculadora de Temperatura
Crie uma classe Temperatura.
Ela não terá atributos.

Crie apenas dois métodos estáticos:
celsius_para_fahrenheit(c)
fahrenheit_para_celsius(f)

## Exercício 8.1 — Classe Livro (__str__)
Crie uma classe Livro.

Atributos:
titulo
autor
ano

Método especial:
Implemente __str__.

## Exercício 8.2 — Retângulo (__eq__)
Reutilize a classe Retangulo da Aula 6.

Requisitos:
Implemente apenas o método __eq__.

Dois retângulos serão iguais quando:
base igual
altura igual