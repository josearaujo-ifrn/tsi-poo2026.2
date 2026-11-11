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


### 🏆 **Desafio Integrador Final 2 — Projeto Modular em Camadas (E-Commerce Delivery)**

Você deverá construir um sistema completo de **Gestão de Pedidos e Delivery**, estruturado em **módulos e pacotes separados**, aplicando **todos os conceitos estudados nos 4 blocos** e os recursos avançados da prova.

---

### 📁 **Estrutura de Pastas e Módulos Exigida**

Seu projeto deve ser organizado na seguinte estrutura de arquivos:

```
sistema_ecommerce/
│
├── excecoes/
│   ├── __init__.py
│   └── customizadas.py         # Exceções personalizadas do sistema
│
├── mixins/
│   ├── __init__.py
│   └── notificavel.py          # Mixin para notificações do sistema
│
├── modelos/
│   ├── __init__.py
│   ├── produto.py              # ABC, @property, @classmethod, @staticmethod, Dunders
│   └── item_pedido.py          # Dataclass, Agregação do Produto
│
├── servicos/
│   ├── __init__.py
│   ├── notificadores.py        # Duck Typing (Email e SMS)
│   └── pedido_service.py       # Regra de negócio, Injeção de Dependência, Composição e SRP
│
└── main.py                     # Ponto de entrada (Imports, Interface CLI, try/except)

```

---

### 📜 **Especificação Detalhada por Módulo**

#### 1\. `excecoes/customizadas.py`

Crie duas exceções customizadas herdando de `Exception`:

* `EstoqueInsuficienteError(Exception)`
* `CupomInvalidoError(Exception)`

---

#### 2\. `mixins/notificavel.py`

Crie a classe **NotificavelMixin**:

* Possui o método `notificar(self, mensagem: str) -&gt; None` que exibe a mensagem formatada com `[NOTIFICAÇÃO SISTEMA]: {mensagem}`.

---

#### 3\. `modelos/produto.py`

Neste módulo, implementaremos **Herança, ABC,** **@property** **,** **@classmethod** **,** **@staticmethod** **e Dunders**:

1. **Classe Abstrata** **Produto(ABC)**:
  * **Atributos protegidos**: `_nome: str`, `_codigo: str`, `_preco: float` e `validade: date`.
  * **Validação com** **@property**:
    * `preco`: o setter deve garantir que o preço seja estritamente maior que zero (`&lt;= 0` lança `ValueError("O preço deve ser maior que zero.")`).
  * **Método de Classe (** **@classmethod** **)**:
    * `de_string(cls, texto: str) -&gt; "Produto"`: recebe uma string no formato `"TIPO;Nome;Codigo;Preco;AAAA-MM-DD;EXTRAS"` (onde TIPO pode ser `"FISICO"` ou `"DIGITAL"`) e retorna a instância correta da subclasse (`ProdutoFisico` ou `ProdutoDigital`).
  * **Método Estático (** **@staticmethod** **)**:
    * `calcular_imposto_padrao(valor: float) -&gt; float`: retorna `valor * 0.10` (10% de imposto base).
  * **Métodos Especiais (Dunders)**:
    * `__str__(self) -&gt; str`: exibição legível do produto.
    * `__repr__(self) -&gt; str`: representação técnica de depuração.
    * `__eq__(self, outro: object) -&gt; bool`: dois produtos são iguais se possuem o mesmo `_codigo`.
    * `__lt__(self, outro: "Produto") -&gt; bool`: compara produtos pela data de `validade` (para permitir ordenação via `sorted()`).
  * **Método Abstrato**:
    * `@abstractmethod def calcular_preco_final(self) -&gt; float`: assinatura obrigatória para as subclasses.
2. **Subclasse** **ProdutoFisico(Produto)**:
  * Herda de `Produto`.
  * Atributo adicional: `peso_kg: float`.
  * Sobrescreve `calcular_preco_final(self) -&gt; float`: calcula o frete como `peso_kg * 5.0` e retorna `self.preco + frete`. Usa `super().__init__()`.
3. **Subclasse** **ProdutoDigital(Produto)**:
  * Herda de `Produto`.
  * Atributo adicional: `tamanho_mb: float`.
  * Sobrescreve `calcular_preco_final(self) -&gt; float`: retorna diretamente `self.preco` (sem frete). Usa `super().__init__()`.

---

#### 4\. `modelos/item_pedido.py`

Crie uma **Dataclass**:

* `@dataclass` **ItemPedido**:
  * Campos: `produto: Produto` (**Agregação**) e `quantidade: int`.
  * Método: `subtotal(self) -&gt; float`, que retorna `self.produto.calcular_preco_final() * self.quantidade`.

---

#### 5\. `servicos/notificadores.py`

Implemente o **Duck Typing**:

* Crie duas classes independentes sem superclasse comum: **NotificadorEmail** e **NotificadorSMS**.
* Ambas devem ter a mesma assinatura de método: `enviar(self, destinatario: str, mensagem: str) -&gt; None`.
  * `NotificadorEmail`: imprime `f"[E-MAIL para {destinatario}]: {mensagem}"`.
  * `NotificadorSMS`: imprime `f"[SMS para {destinatario}]: {mensagem}"`.

---

#### 6\. `servicos/pedido_service.py`

Neste módulo de Regra de Negócio (SRP), teremos **Injeção de Dependência, Composição e Mixin**:

* **Classe** **PedidoService(NotificavelMixin)**:
  * **Injeção de Dependência**: no `__init__`, recebe por parâmetro o `notificador` (Duck Typing) e o `cliente_email: str`.
  * **Composição**: no `__init__`, cria internamente o seu próprio atributo `self.historico_status: list[str] = []` e adiciona `"Pedido Criado"`.
  * Atributo de lista: `self.itens: list[ItemPedido] = []`.
  * Método `adicionar_item(self, produto: Produto, quantidade: int) -&gt; None`:
    * Se `quantidade &lt;= 0`, lança `EstoqueInsuficienteError("Quantidade inválida para item.")`.
    * Instancia o `ItemPedido` e o adiciona à lista de itens.
  * Método `calcular_total(self) -&gt; float`:
    * Retorna a soma do subtotal de todos os itens.
  * Método `finalizar_pedido(self, cupom: str = None) -&gt; float`:
    * Se `cupom == "INVALIDO"`, lança `CupomInvalidoError("Cupom de desconto expirado ou inexistente.")`.
    * Se `cupom == "PROMO10"`, aplica 10% de desconto sobre o total final.
    * Envia a notificação do cliente chamando `self.notificador.enviar(self.cliente_email, ...)` (Duck Typing).
    * Usa o método `self.notificar(...)` herdado do `NotificavelMixin`.
    * Atualiza o histórico de status interno registrando `"Pedido Finalizado"`.
    * Retorna o valor total a ser pago.

---

#### 7\. `main.py`

Ponto de entrada da aplicação:

* **Imports Limpos**: importações relativas/absolutas dos pacotes (`from modelos.produto import ...`, `from servicos.pedido_service import ...`, etc.).
* **Execução Completa**:
  1. Instanciação de produtos via construtor tradicional e via `@classmethod de_string()`.
  2. Teste de Dunders (`print`, `repr`, comparação `==` e ordenação de produtos por data de validade usando `sorted()`).
  3. Instanciação do serviço de pedido injetando o notificador de e-mail/SMS.
  4. Adição de itens e finalização do pedido.
  5. Captura de exceções com blocos `try/except` simulando falha por cupom inválido, preço negativo no setter e quantidade inválida.
  6. Exibição do histórico do pedido.