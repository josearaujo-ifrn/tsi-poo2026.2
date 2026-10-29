from dataclasses import dataclass
# === Aula 22 - Dataclasses ===
# item 1

@dataclass
class Produto:
    nome: str
    preco: float

class ItemPedido:
    produto: Produto
    quantidade: int

    @property
    def subtotal(self) -> float:
        return self.produto.preco * self.quantidade

class Pedido:
    def __init__(self, cliente: "Cliente") -> None:
        self.cliente = cliente # associação
        self._itens: list[ItemPedido] = []

    def adicionar(self, produto: Produto, quantidade: int) -> None:
        item = ItemPedido(produto, quantidade)
        self._itens.append(item) # composição

    @property
    def total(self) -> float:
        return sum(i.subtotal for i in self._itens)

class Cliente:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self._pedidos: list[Pedido] = []

# item 2

@dataclass(order = True)
class Musica:
    titulo: str
    artista: str
    duracao_segundos: int

playlist = (Musica("m2","a2", 20), Musica("m1", "a1", 10))
print(sorted(playlist))

# item 3

@dataclass(frozen = True)
class Endereco:
    rua: str
    numero: int
    cidade: str
    estado: str

en1 = Endereco("rua vinte e cinco de março", 100, "São Paulo", "São Paulo")
en1.rua = "avenida paulista" # ao tentar mudar o endereço,
# nao vai funcionar devido ao frozen true

# item 4
@dataclass(order=True)
class Aluno:
    media: float
    nome: str
    
turma = [Aluno(8.5, "Bia"), Aluno(9.1, "Ana")]
print(sorted(turma)) # __lt__ gerado!

# item 5
# nao deveria, a conta bancaria deve ter validaçoes, como numero da conta/agencia,
# que nao devem ser vazios ou nao devem ter letras 
# e o saldo da conta nao pode ser negativo  