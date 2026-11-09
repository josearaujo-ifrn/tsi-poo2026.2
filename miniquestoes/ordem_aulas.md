#### **Bloco 1: Relacionamentos entre Objetos**

* [X] **Mini-aula 1 — Associação**: Relação de uso ("A usa B"), passagem por parâmetro e exemplo `Pessoa` \+ `Interruptor`. *FINALIZADO*
* [X] **Mini-aula 2 — Agregação**: Relação de posse ("A tem B"), partes criadas fora e armazenadas em atributos/coleções, exemplo `CarrinhoDeCompras` \+ `Produto`. *FINALIZADO*
* [X] **Mini-aula 3 — Composição**: Relação de criação todo/parte ("A é composto por B"), criação dentro do `__init__`, ciclo de vida atrelado, exemplo `Conta` \+ `Historico`. *FINALIZADO*
* [X] **Mini-aula 4 — Comparativo &amp; Modelagem dos 3 Relacionamentos**: Matriz de decisão ("precisa lembrar?", "quem cria?"), Notação UML (seta, losango aberto, losango fechado) e modelagem de sistema completo (`Cliente`, `Pedido`, `Produto`, `ItemPedido`). *FINALIZADO*

#### **Bloco 2: Herança e Hierarquias**

* [X] **Mini-aula 5 — Herança Simples e Sobrescrita**: Relação "É UM", reutilização de código com `super().__init__()`, sobrescrita de métodos, exemplo `Animal`/`Gato`/`Cachorro` e duelo "é um" vs. "tem um". *FINALIZADO*
* [X] **Mini-aula 6 — Herança Múltipla e MRO**: Múltiplas superclasses, uso seguro de Mixins (`Autenticavel`), problema do diamante e Ordem de Resolução de Métodos (`__mro__`). *FINALIZADO*
* [X] **Desafio Integrador**: Desafio com Associação, Agregação, Composição, Herança Simples, Sobrescrita e Mixin (Herança Múltipla). *FINALIZADO*

#### **Bloco 3: Polimorfismo, Injeção e Abstração**

* [X] **Mini-aula 7 — Polimorfismo e Duck Typing**: Mesma mensagem para múltiplos objetos, polimorfismo por herança vs. Duck Typing ("se anda e grasna como pato..."), sobrecarga de operadores (`dunders`). *FINALIZADO*
* [X] **Mini-aula 8 — Injeção de Dependência**: Inversão de Controle (IoC), passagem de dependências pelo construtor e facilidade de testes. *FINALIZADO*
* [ ] **Mini-aula 9 — Classes e Métodos Abstratos (ABC)**: Garantia de contratos explícitos com `ABC` e `@abstractmethod`, impedimento de instanciação genérica e implementação obrigatória nas subclasses.

#### **Bloco 4: Recursos Avançados, Organização e Revisão**

* [ ] **Mini-aula 10 — Dataclasses**: Eliminação de boilerplate com `@dataclass`, uso de `field(default_factory=...)`, imutabilidade (`frozen=True`), ordenação e quando utilizar classe convencional vs. dataclass.
* [ ] **Mini-aula 11 — Organização de Software e Arquitetura**: Módulos e pacotes, alta coesão e baixo acoplamento, Princípio da Responsabilidade Única e estrutura de referência para projetos.
* [ ] **Mini-aula 12 — Revisão Geral e Resolução de Exercícios Práticos**: Análise de cenários complexos (estilo sistema de Delivery), mapeamento de substantivos/verbos para classes/métodos e checklist de erros comuns.