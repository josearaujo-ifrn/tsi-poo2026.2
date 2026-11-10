### Exercício 1.2 — Complete o Código 
Monte o método `dirigir` na classe `Motorista` de modo que ele receba um objeto `Veiculo` como parâmetro e chame seu método `ligar()`:
class Veiculo:
    def ligar(self):
        print("Veículo ligado e pronto para rodar!")

class Motorista:
    def __init__(self, nome: str):
        self.nome = nome

    # Escreva aqui o método dirigir que recebe o veículo por parâmetro

### **Exercício 2.2 — Complete o Código** 
Monte a classe `Biblioteca` que agrega objetos da classe `Livro` em uma lista e possui um método para listar todos os livros cadastrados:
class Livro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self, nome: str):
        self.nome = nome
        # 1. Crie a lista vazia para armazenar os livros

    def adicionar_livro(self, livro: Livro):
        # 2. Adicione o livro na lista interna

    def exibir_livros(self):
        # 3. Imprima o título e o autor de cada livro agregado
        pass
# Teste seu código instanciando 2 livros e adicionando à biblioteca!

### **Exercício 3.2 — Complete o Código** 
Implemente o relacionamento de **Composição** entre a classe `Pessoa` e a classe `Endereco`. Ao instanciar uma `Pessoa`, ela deve criar internamente o seu próprio objeto `Endereco` com a rua e a cidade fornecidas:

class Endereco:
    def __init__(self, rua: str, cidade: str) -> None:
        self.rua = rua
        self.cidade = cidade

    def obter_formatado(self) -> str:
        return f"{self.rua}, {self.cidade}"

class Pessoa:
    def __init__(self, nome: str, rua: str, cidade: str) -> None:
        self.nome = nome
        # 1. Crie o objeto Endereco DENTRO do __init__ (Composição)

    def exibir_dados(self) ->; None:
        # 2. Imprima o nome e o endereço formatado chamando o método do Endereco interno
        pass

# Teste seu código instanciando apenas uma Pessoa (sem instanciar Endereco fora):
# p = Pessoa("Carlos", "Av. Paulista", "São Paulo")
# p.exibir_dados()

### **Exercício 4.1 — Sistema de Universidade**
# 📜 Descrição do Cenário:
Você foi contratado(a) para modelar o sistema de uma **Universidade**.
1. **Classe** **Projetor**:
  * Possui o método `exibir_slides()` que imprime uma mensagem como `"Exibindo slides da aula..."`.
2. **Classe** **Professor**:
  * Possui o atributo `nome`.
  * Possui um método `dar_aula()` que recebe um objeto `Projetor` como parâmetro e chama o método de exibir slides. *(Atenção: Qual é o tipo de relacionamento aqui?)*
3. **Classe** **GradeCurricular**:
  * Possui o atributo `curso` (ex: `"Ciência da Computação"`).
  * Possui o método `detalhar()` que imprime o nome do curso.
4. **Classe** **Universidade**:
  * Possui o atributo `nome`.
  * Quando uma `Universidade` é instanciada no seu `__init__`, ela cria automaticamente a sua própria `GradeCurricular` interna. *(Atenção: Qual é o tipo de relacionamento aqui?)*
  * A `Universidade` possui uma lista interna para guardar `Professor`es.
  * Possui um método `contratar_professor()` que recebe um `Professor` já existente e o adiciona à lista. *(Atenção: Qual é o tipo de relacionamento aqui?)*
  * Possui um método `relatorio()` que exibe o nome da universidade, os detalhes da grade curricular e o nome de todos os professores contratados.

### 📝 Exercicio 5.1 — Aula 5
Crie uma superclasse `Veiculo` e duas subclasse `Carro` e `Moto`:

1. **Superclasse** **Veiculo**:
  * Contém os atributos `marca` e `modelo`.
  * Contém o método `acelerar()` que imprime `"Veículo acelerando..."`.
2. **Subclasse** **Carro**:
  * Herda de `Veiculo`.
  * Possui o atributo adicional `qtd_portas`.
  * Usa `super().__init__()`.
  * Sobrescreve o método `acelerar()` para imprimir `"Carro [marca] [modelo] acelerando com [qtd_portas] portas!"`.


#### 📜 Exercicio 6.1 - Aula 6
1. **Crie a superclasse base** **Documento**:
  * O `__init__` deve receber o atributo `titulo` (string) e `conteudo` (string).
2. **Crie o Mixin** **ExportavelJSONMixin**:
  * Não precisa de `__init__`.
  * Possui o método `para_json(self) -&gt; str` que converte e retorna uma string simulando formato JSON. Por exemplo: `f'{{"titulo": "{self.titulo}", "conteudo": "{self.conteudo}"}}'` *(Atenção: o Mixin assume que quem o herdar terá os atributos* *titulo* *e* *conteudo* *!)*
3. **Crie a subclasse** **RelatorioFinanceiro**:
  * Herda de `Documento` **E** de `ExportavelJSONMixin` (Herança Múltipla).
  * O `__init__` recebe `titulo`, `conteudo` e o atributo específico `valor_total` (float), utilizando `super().__init__(titulo, conteudo)` para reaproveitar a base.
4. **Teste seu código**:
  * Instancie um `RelatorioFinanceiro("Balanço Q3", "Lucro líquido elevado", 150000.0)`.
  * Imprima o resultado da chamada do método `.para_json()`.


### 🔥 **Super Desafio Integrador do Bloco 2: Sistema de Gestão de Frota e Logística**

Este desafio junta **TUDO** o que aprendemos até agora: **Associação, Agregação, Composição, Herança Simples, Sobrescrita e Mixin (Herança Múltipla)**!

#### 📜 Descrição do Sistema:

1. **Mixin** **NotificavelMixin**:
  * Possui o método `notificar(self, mensagem: str) -&gt; None` que imprime: `f"[NOTIFICAÇÃO]: {mensagem}"`.
2. **Superclasse** **Veiculo**:
  * `__init__`: recebe `placa` (str) e `capacidade_carga` (float).
  * Método `calcular_custo_viagem(self, distancia_km: float) -&gt; float`: retorna o custo base calculado como `distancia_km * 2.0`.
3. **Subclasse** **Caminhao** **(Herda de** **Veiculo** **)**:
  * `__init__`: recebe `placa`, `capacidade_carga` e `qtd_eixos` (int). Usa `super().__init__()`.
  * **Sobrescrita**: Sobrescreve `calcular_custo_viagem(self, distancia_km: float) -&gt; float`:
    * Obtém o custo base chamando o método da classe pai com `super()`.
    * Adiciona um valor de pedágio extra: `qtd_eixos * 50.0`.
    * Retorna o valor total.
4. **Classe** **Motorista**:
  * `__init__`: recebe `nome` (str) e `cnh` (str).
5. **Classe** **Rota**:
  * `__init__`: recebe `origem` (str), `destino` (str) e `distancia_km` (float).
  * Método `detalhar(self) -&gt; str`: retorna algo como `f"{self.origem} -&gt; {self.destino} ({self.distancia_km} km)"`.
6. **Classe** **GPS**:
  * Método `calcular_tempo(self, distancia_km: float) -&gt; None`: imprime `f"[GPS]: Tempo estimado para {distancia_km} km é de {distancia_km / 60:.1f} horas."`.
7. **Classe** **Viagem** **(Herda de** **NotificavelMixin** **)**:
  * **Composição**: No `__init__`, recebe `origem`, `destino` e `distancia_km`, e **instancia internamente** o seu próprio objeto `Rota`.
  * **Agregação**: No `__init__`, recebe também um objeto `veiculo` (do tipo `Veiculo`) e um objeto `motorista` (do tipo `Motorista`), ambos criados fora.
  * **Associação**: Possui o método `iniciar_viagem(self, gps: GPS) -&gt; None`:
    * Recebe o objeto `gps` por parâmetro.
    * Chama o método `gps.calcular_tempo(...)` usando a distância da rota.
    * Chama o método `self.notificar(...)` (herdado do Mixin) avisando que a viagem do motorista X com o veículo de placa Y começou.
  * Método `resumo(self) -&gt; None`:
    * Imprime o motorista, a placa do veículo, a rota detalhada e o custo total da viagem (chamando `veiculo.calcular_custo_viagem`).

### 🧪 Roteiro de Teste do Script:

1. Instancie um `Motorista` ("Carlos", "123456").
2. Instancie um `Caminhao` ("ABC-1234", 15000.0, qtd\_eixos=4).
3. Instancie um `GPS`.
4. Instancie uma `Viagem` (passando a origem `"Rio de Janeiro"`, destino `"São Paulo"`, distância `430.0`, o caminhão e o motorista).
5. Inicie a viagem passando o `gps`.
6. Exiba o resumo da viagem!


### 📝 Exercicio 7.1 — Aula 7

Crie duas classes independentes sem nenhuma herança entre elas: `NotificadorEmail` e `NotificadorSMS`.

1. **Classe** **NotificadorEmail**:
  * Método `enviar(self, mensagem: str) -&gt; None`: imprime `f"Enviando E-mail: {mensagem}"`.
2. **Classe** **NotificadorSMS**:
  * Método `enviar(self, mensagem: str) -&gt; None`: imprime `f"Enviando SMS: {mensagem}"`.
3. **Função Polimórfica** **enviar\_alerta(notificador, mensagem: str) -&gt; None**:
  * Recebe um objeto `notificador` generico e uma `mensagem`, e chama `notificador.enviar(mensagem)`.

  ### 📝 Exercício 8.1 — Aula 8
Vamos exercitar a Injeção de Dependência!

1. Crie duas classes de banco de dados independentes: `BancoMySQL` e `BancoPostgreSQL`.
  * Ambas devem ter um método `salvar(self, dados: str) -&gt; None`.
  * `BancoMySQL`: imprime `f"Salvando '{dados}' no banco MySQL..."`.
  * `BancoPostgreSQL`: imprime `f"Salvando '{dados}' no banco PostgreSQL..."`.
2. Crie a classe `UsuarioService`:
  * Seu `__init__` deve receber a dependência do banco de dados (`banco`) e armazená-la.
  * Possui o método `registrar_usuario(self, nome: str) -&gt; None` que chama `self.banco.salvar(f"Usuário {nome}")`.
3. Instancie o `UsuarioService` duas vezes: uma injetando o `BancoMySQL` e outra injetando o `BancoPostgreSQL`, e registre um usuário em cada.

### 📝 Exercício 9.1 — Aula 9

Crie uma estrutura de **Formas Geométricas** utilizando uma **Classe Abstrata**:

1. **Classe Abstrata** **Forma** **(Herda de** **ABC** **)**:
  * Possui o método abstrato `@abstractmethod` chamado `calcular_area(self) -&gt; float`.
2. **Subclasse** **Quadrado**:
  * Herda de `Forma`.
  * Seu `__init__` recebe `lado: float`.
  * Implementa obrigatoriamente o método `calcular_area()` retornando `lado * lado`.
3. **Subclasse** **Circulo**:
  * Herda de `Forma`.
  * Seu `__init__` recebe `raio: float`.
  * Implementa obrigatoriamente o método `calcular_area()` retornando `3.14 * (raio ** 2)`.


  #### **Super Desafio Integrador do Bloco 3: Sistema de Checkout e Processamento de Pagamentos**

1. **Classe Abstrata** **MetodoPagamento** **(Herda de** **ABC** **)**:
  * O `__init__` recebe `valor: float`.
  * Possui o método abstrato `@abstractmethod` denominado `processar_pagamento(self) -&gt; bool`.
2. **Subclasses Concretas de Pagamento**:
  * **PagamentoCartao** (Herda de `MetodoPagamento`):
    * O `__init__` recebe `valor: float` e `numero_cartao: str` (usa `super().__init__`).
    * Implementa `processar_pagamento(self) -&gt; bool`: exibe `f"Pagamento de R$ {self.valor:.2f} aprovado no Cartão {self.numero_cartao}."` e retorna `True`.
  * **PagamentoPix** (Herda de `MetodoPagamento`):
    * O `__init__` recebe `valor: float` e `chave_pix: str` (usa `super().__init__`).
    * Implementa `processar_pagamento(self) -&gt; bool`: exibe `f"Pagamento de R$ {self.valor:.2f} aprovado via PIX ({self.chave_pix})."` e retorna `True`.
3. **Serviços de Notificação (Duck Typing)**:
  * Crie duas classes totalmente independentes (sem superclasse comum): **NotificadorEmail** e **NotificadorSMS**.
  * Ambas devem ter exatamente o mesmo método: `enviar_notificacao(self, mensagem: str) -&gt; None`.
  * `NotificadorEmail`: exibe `f"[E-MAIL]: {mensagem}"`.
  * `NotificadorSMS`: exibe `f"[SMS]: {mensagem}"`.
4. **Classe** **Checkout**:
  * **Injeção de Dependência**: O `__init__` recebe por parâmetro o objeto `notificador` (que utilizará Duck Typing para chamar `.enviar_notificacao()`).
  * Método **realizar\_checkout(self, pagamento: MetodoPagamento) -&gt; None**:
    * Recebe um objeto do tipo `MetodoPagamento` (Polimorfismo).
    * Chama `sucesso = pagamento.processar_pagamento()`.
    * Se `sucesso` for `True`, chama o notificador injetado enviando a mensagem: `f"Confirmação: Pagamento de R$ {pagamento.valor:.2f} concluído!"`

### Exercicio 10.1 — Aula 10

Crie uma Dataclass para representar um **Item de Pedido**:

1. Use o decorador `@dataclass`.
2. A classe `Item` deve ter os campos:
  * `nome: str`
  * `preco_unitario: float`
  * `quantidade: int`
3. Crie um método normal dentro da dataclass chamado `calcular_total(self) -&gt; float` que retorna `preco_unitario * quantidade`.
4. Instancie 1 item, imprima a representação automática dele e exiba o resultado do método `calcular_total()`.

### Exercício 11.1 — Aula 11

Analise a classe abaixo que viola o **Princípio da Responsabilidade Única (SRP)** por misturar regra de negócio com interface do usuário:

# CÓDIGO COM PROBLEMA DE DESIGN:
class ContaCorrente:
    def __init__(self, saldo: float) -&gt; None:
        self.saldo = saldo

    def sacar_com_interface(self) -&gt; None:
        # A classe de negócio está fazendo input() e print() diretamente!
        valor = float(input("Digite o valor do saque: "))
        if valor &lt;= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado! Saldo atual: R$ {self.saldo:.2f}")
        else:
            print("Erro: Saldo insuficiente!")

**Sua Tarefa de Refatoração:**

1. Refatore a classe `ContaCorrente` para que ela seja uma classe pura de regra de negócio (sem `input()` e sem `print()`). O método `sacar(self, valor: float) -&gt; bool` deve apenas realizar a subtração se houver saldo suficiente e retornar `True` (se conseguiu sacar) ou `False` (se não houver saldo).
2. Escreva fora da classe (simulando a função/ponto de entrada da interface) a lógica que lê a entrada do usuário (`valor`), chama o método `sacar()` da conta e exibe a mensagem de sucesso ou erro com base no retorno booleano.

### 🏆 **Desafio Integrador Final 1 — Prova Prática de POO**

Inspirado diretamente na estrutura oficial da sua avaliação (`POO_-_Aval1_-_E1-T6.1.pdf`), este desafio avalia a construção de uma solução completa em **um único arquivo Python**, contendo construtor, propriedades validadas, métodos estáticos/de classe, dunders, exceções customizadas e métodos de negócio.

---

#### 📌 **Contexto da Prova:**

O almoxarifado de um laboratório de pesquisas precisa controlar, de forma individual, os lotes de **Reativos Químicos** mantidos em estoque. Cada lote possui um nome de reativo, um código de lote, uma data de validade, uma quantidade de frascos disponíveis e um custo por frasco.

---

#### 📜 **Requisitos da Avaliação (5 Itens de 10 Pontos Cada):**

* **Item 1 (PEP 8 & Type Hints - Avaliação Transversal)**:
  * Nomes de classe (`ReativoQuimico`), atributos, métodos e exceções devem seguir rigorosamente a PEP 8.
  * **Todos** os parâmetros, atributos e retornos de método devem conter **Type Hints** explícitos (`str`, `int`, `float`, `date`, `bool`, `None`).
* **Item 2 (Construtor e Encapulamento com** **@property** **)**:
  * Defina o construtor `__init__(self, nome: str, codigo_lote: str, validade: date, quantidade: int, custo_unitario: float)`.
  * Os atributos `quantidade` e `custo_unitario` devem ser protegidos (ex: `_quantidade` e `_custo_unitario`) e expostos através de `@property` com setters de validação:
    * `quantidade` não pode ser negativa (`< 0`). Caso contrário, lance `ValueError("A quantidade não pode ser negativa.")`.
    * `custo_unitario` deve ser estritamente maior que zero (`<= 0` lança erro). Caso contrário, lance `ValueError("O custo unitario deve ser maior que zero.")`.
    * As validações devem ser aplicadas tanto no construtor quanto em qualquer atribuição posterior.
* **Item 3 (** **@classmethod** **e** **@staticmethod** **)**:
  * Implemente o método de classe `@classmethod` chamado `de_string(cls, texto: str) -> "ReativoQuimico"`, que receba uma string no formato `"nome;codigo_lote;AAAA-MM-DD;quantidade;custo_unitario"` e retorne uma instância de `ReativoQuimico`.
  * Implemente o método estático `@staticmethod` chamado `dias_para_vencer(validade: date) -> int`, que receba uma data de validade e retorne quantos dias faltam em relação a `date.today()`.
* **Item 4 (Métodos Especiais / Dunders)**:
  * `__str__(self) -> str`: retorna a descrição legível (ex: `"Reativo: Ácido Clorídrico | Lote: L2026X | Qtd: 15 | Validade: 2026-12-31"`).
  * `__repr__(self) -> str`: retorna a representação técnica para depuração.
  * `__eq__(self, outro: object) -> bool`: dois reativos são iguais se possuem o mesmo `nome` e o mesmo `codigo_lote`.
  * `__lt__(self, outro: "ReativoQuimico") -> bool`: compara dois objetos pela data de `validade`, permitindo que uma lista de reativos seja ordenada via `sorted()` da validade mais próxima para a mais distante.
* **Item 5 (Exceções Customizadas e Regras de Negócio)**:
  * Crie duas exceções customizadas herdando de `Exception`: `QuantidadeInvalidaError` e `ReativoVencidoError`.
  * Implemente o método `retirar_do_estoque(self, qtd: int) -> None`:
    * Lance `QuantidadeInvalidaError` se `qtd <= 0` ou se `qtd > self.quantidade`.
    * Lance `ReativoVencidoError` se a data de validade já tiver passado (`self.validade < date.today()`).
    * Se tudo estiver válido, reduza a quantidade do estoque.
  * Implemente o método `repor_estoque(self, qtd: int) -> None`: aumenta a quantidade no estoque reaproveitando o setter validado.

---

#### 🧪 **Bloco de Demonstração Obrigatorio:**

No final do arquivo, inclua o bloco `if __name__ == "__main__":` demonstrando:

1. Criação de instâncias normais e via `de_string()`.
2. Teste do `dias_para_vencer()`.
3. Execução de `retirar_do_estoque()` e `repor_estoque()`.
4. Captura com `try/except` dos casos de erro (`QuantidadeInvalidaError`, `ReativoVencidoError` e `ValueError` do setter).
5. Comparação `==` e ordenação de uma lista de lotes com `sorted()`.