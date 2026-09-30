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
        return cls( no, lo, data, int(qua), int(valo) )
    @staticmethod
    def dias_para_vencer(data: date):
        hoje = date.today()
        dif = hoje - data
        return dif

    @property
    def valor(self):
        return self._valor

    @property
    def quantidade(self):
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
        elif quantidade > self.quantidade:
            raise QuantidadeInvalidaError("Erro: o estoque não possui toda essa quantidade.")
        else:
            self.quantidade -= quantidade

    def repor(self, quantidade: int):
        if quantidade <= 0:
            raise QuantidadeInvalidaError("Erro: a quantidade de reposição não pode ser negativa ou zero.")
        else:
            self.quantidade += quantidade

    def __str__(self):
        return \
        f"Medicamento: {self.nome}\nLote: {self.lote}\nValidade: {self.validade}\nQuantidade: {self.quantidade}\nValor: {self.valor}"

    def __eq__(self, outro: str):
        if isinstance(outro, Medicamento):
            return self.nome == outro.nome and self.lote == self.lote
        else:
            return False

    def __lt__(self, outro: "Medicamento"):
        return self.validade < outro.validade

    def __repr__(self):
        return f"Medicamento(nome={self.nome}), Preço(preco={self.valor})"
try:
    m1 = Medicamento("a", "b1", date(2026, 10, 11), 5, 10.00)
    m2 = Medicamento("b", "b1", date(2026, 11, 11), 5, 12.50)
    m3 = Medicamento("c","b1", date(2026, 12, 11), 5, 15.00)
    medicamentos = [m1, m2, m3]
    for medicamento in sorted(medicamentos):
        print(medicamento)
except MedicamentoVencidoError as erro:
    print(erro)
except QuantidadeInvalidaError as erro:
    print(erro)
except ValueError as erro:
    print(erro)