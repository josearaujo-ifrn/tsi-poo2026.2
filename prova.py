from datetime import date

class QuantidadeInvalidaError(Exception):
    pass # criei uma classe com exception e pass para servir de "base" (pendente)
class MedicamentoVencidoError(Exception):
    pass # criei uma classe com exception e pass para servir de "base" (pendente)

class Medicamento:
    def __init__(self, nome: str, lote: str, validade: date, quantidade: int, valor: float):
        self.nome = nome
        self.lote = lote
        self.validade = validade
        self.quantidade = quantidade
        self.valor = valor

    @classmethod
    def de_registro(cls, texto: str) -> "Medicamento":
        no, lo, vali, qua, valo = texto.split(";")
        data = date.fromisoformat(vali)
        return cls( no, lo, data, int(qua), float(valo) )
    @staticmethod
    def dias_para_vencer(data: date):
        hoje = date.today()
        dif = hoje - data
        return dif

    @property
    def valor(self) -> int:
        return self._valor

    @property
    def quantidade(self) -> int:
        return self._quantidade

    @valor.setter
    def valor(self, valor):
        if valor <= 0:
            raise ValueError("Erro: o valor do medicamento deve ser maior que 0.")
        else:
            self._valor = valor

    @quantidade.setter
    def quantidade(self, quantidade):
        if quantidade < 0:
            raise QuantidadeInvalidaError("Erro: o medicamento não deve ter quantidade negativa.")
        else:
            self._quantidade = quantidade

    def dispensar(self, quantidade: int): # falta validaçao da validade
        if quantidade <= 0:
            raise QuantidadeInvalidaError("Erro: a quantidade de saída não pode ser negativa ou zero.")
        if quantidade > self.quantidade:
            raise QuantidadeInvalidaError("Erro: o estoque não possui toda essa quantidade.")
        if self.validade <= date.today():
            raise MedicamentoVencidoError("Erro: o medicamento está vencido.")
        else:
            self.quantidade -= quantidade

    def repor(self, quantidade: int):
        if quantidade <= 0:
            raise QuantidadeInvalidaError("Erro: a quantidade de reposição não pode ser negativa ou zero.")
        else:
            self.quantidade += quantidade

    def __str__(self) -> str:
        return \
        f"Medicamento: {self.nome}\nLote: {self.lote}\nValidade: {self.validade}\nQuantidade: {self.quantidade}\nValor: {self.valor}\n"

    def __eq__(self, outro: str) -> bool:
        if isinstance(outro, Medicamento):
            return self.nome == outro.nome and self.lote == self.lote
        else:
            return False

    def __lt__(self, outro: "Medicamento") -> bool:
        return self.validade < outro.validade

    def __repr__(self) -> str:
        return f"Medicamento(nome={self.nome}), Preço(preco={self.valor})"
# try:
#     m1 = Medicamento("a", "b1", date(2026, 10, 11), 5, 10.00)
#     m2 = Medicamento("b", "b1", date(2026, 11, 11), 5, 12.50)
#     m3 = Medicamento("c","b1", date(2026, 12, 11), 5, 15.00)
#     medicamentos = [m1, m2, m3]
#     for medicamento in sorted(medicamentos):
#         print(medicamento)
# except MedicamentoVencidoError as erro:
#     print(erro)
# except QuantidadeInvalidaError as erro:
#     print(erro)
# except ValueError as erro:
#     print(erro)

if __name__ == "__main__":
    m1 = Medicamento("Dipirona 500mg", "L2026A", date(2026, 12, 31), 100, 12.50)
    m2 = Medicamento.de_registro("Amoxicilina 500mg;L2026B;2026-10-15;40;18.90")
    # print(f"Dados de m1: {m1}") # ex.: Dipirona 500mg (L2026A) - 100 un. - val. 31/12/2026
    # print(f"Dados de m2: {m2}") # ex.: Amoxicilina 500mg (L2026B) - 40 un. - val. 15/10/2026
    # print(f"Dias para vencer de m2: {Medicamento.dias_para_vencer(m2.validade)}")
    # print("Dispensando 20 medicamentos de m1")
    # m1.dispensar(20)
    # print(f"Quantidade de m1: {m1.quantidade}")

    vencido = Medicamento("Soro Fisiológico", "L2025X", date(2025, 1, 10), 10, 5.0)
    # try:
    #     vencido.dispensar(1)
    # except MedicamentoVencidoError as erro:
    #     print(erro)

    outro = Medicamento("Dipirona 500mg", "L2026A", date(2026, 1, 1), 0, 1.0)
    print(f"m1 é igual a outro? {m1 == outro}")

    estoque = [m1, m2, vencido, outro]
    print("Exibindo lista ordenada por data (mais antigos primeiro): ")
    for lote in sorted(estoque):
        print(lote)

    try:
        m1.quantidade = -5
    except ValueError as erro:
        print(f"Erro esperado: {erro}")
    except QuantidadeInvalidaError as erro:
        print(erro)