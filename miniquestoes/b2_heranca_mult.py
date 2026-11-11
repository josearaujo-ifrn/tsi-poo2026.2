# Exercicio 06 - Aula 06: Herança Múltipla e MRO
class Documento:
    def __init__(self, titulo: str, conteudo: str) -> None:
        self.titulo = titulo
        self.conteudo = conteudo

class ExportavelJSONMixin:
    def para_json(self) -> str:
        return f'{{"titulo": "{self.titulo}", "conteudo": "{self.conteudo}"}}'

class RelatorioFinanceiro(Documento, ExportavelJSONMixin):
    def __init__(self, titulo: str, conteudo: str, valor_total: float) -> None:
        super().__init__(titulo, conteudo)
        self.valor_total = valor_total

r = RelatorioFinanceiro("Balanço Q3", "Lucro líquido elevado", 150000.0)
print(r.para_json())