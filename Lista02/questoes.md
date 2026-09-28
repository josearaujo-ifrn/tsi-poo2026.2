## Nível 2 - Aplicação:
■ 6. Classe Funcionario(nome, salario):
– salario como property: rejeitar valores < salário mínimo com SalarioInvalidoError
– aumentar(percentual): apenas 0 < percentual ≤ 30, senão ValueError

■ 7. Classe Email(endereco): property que exige “@” e “.”, senão EmailInvalidoError

■ 8. Teste os dois casos de erro de cada classe com try/except, imprimindo as mensagens

## Nivel 3 - Integração:
■ 9. ContaBancaria completa: _saldo, property saldo (leitura), depositar, sacar
– Exceções: ValorInvalidoError e SaldoInsuficienteError, ambas filhas de ErroDeConta
– Limite de saque por operação: R$ 1.000 → LimiteExcedidoError

■ 10. Programa caixa_eletronico.py: menu em laço (depositar, sacar, saldo, sair)
– Nenhuma entrada do usuário pode derrubar o programa — trate tudo
– O menu captura ErroDeConta para os três erros do domínio