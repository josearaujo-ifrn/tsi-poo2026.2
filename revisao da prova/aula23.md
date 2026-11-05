### Nível 01 -- Compreensão ###
■ 1. Classifique os relacionamentos entre: Pedido→Cliente, Pedido→ItemPedido, Carrinho→Produto, Pessoa→Interruptor
1.1: Cliente tem Pedido // Pedido pertence ao Cliente // Agregação
1.2: Pedido tem ItemPedido // ItemPedido pertence ao Pedido // Agregação
1.3: Carrinho tem Produto // Produto pertence ao Carrinho // Agregação
1.4: Pessoa usa Interruptor // Interruptor é usado por Pessoa // Associação

■ 2. O que acontece se a filha esquecer super().__init__()? Mostre/teste com código
ao esquecer o super init, o filho/a filha nao vai ter seus atributos herdados

■ 3. Sem executar: qual a saída de d.ola() no diamante D(C, B)? Como conferir?
vai sair "Olá de C", pra verificar se usa o metodo "mro", que verifica a ordem da herança

■ 4. Por que “if isinstance(animal, Gato): ... elif ...” é um anti-padrão? Qual a alternativa?
nao é necessario elif, ao verificar usando "if isinstance", os atributos vao ser comparados, pode ser usado "if not isinstance" ou "if isinstance" e "else"

■ 5. Qual a diferença entre um método com pass na superclasse e um @abstractmethod?
ao usar abstractmethod, pode ser deixado um comentario com tres pares de aspas duplas ("""teste"""), diferente do pass, que pode ser esquecido depois

### Nível 02 -- Aplicação ###
■ 6. Veiculo(ABC): placa e diaria; calcular_aluguel(dias) abstrato; descricao() concreto
– Carro (aluguel = diaria × dias) e Moto (20% de desconto sobre o mesmo cálculo)
– Caminhao com taxa fixa de R$ 100 por aluguel — use super() onde couber

■ 7. Locadora que AGREGA veículos: cadastrar, faturamento_previsto(dias) polimórfico

■ 8. Prove com TypeError que Veiculo não instancia
 v = Veiculo("1", 10)
TypeError: Can't instantiate abstract class Veiculo without an implementation for abstract method 'calcular_aluguel'

### Nível 03 -- Integação ###
■ 9. Modele: Restaurante TEM Cardapio (composição); Cardapio agrega Pratos

■ 10. Entregador(ABC) com taxa_entrega(distancia) abstrata; DeBike e DeMoto com regras próprias

■ 11. Pedido: associa Cliente, compõe Itens, recebe um Entregador injetado no construtor
– total = pratos + taxa do entregador — polimorfismo na taxa

■ 12. Exceção EntregaForaDeAreaError para distancia > limite do entregador

■ 13. Programa principal com dois pedidos, entregadores diferentes e o caso de erro tratado