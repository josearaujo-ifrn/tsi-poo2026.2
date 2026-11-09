# # Exercício 01 - Aula 01: Associação
# class Veiculo: 
#     def ligar(self): 
#         print("Veículo ligado e pronto para rodar!")

# class Motorista: 
#     def __init__(self, nome: str): 
#         self.nome = nome 

#     def ligar_veiculo(self, veiculo: Veiculo):
#         veiculo.ligar()

# c = Veiculo()
# m = Motorista("João")
# m.ligar_veiculo(c)

# # Exercício 02 - Aula 02: Agregação
# class Livro:
#     def __init__(self, titulo: str, autor: str) -> None:
#         self.titulo = titulo
#         self.autor = autor

# class Biblioteca:
#     def __init__(self, nome: str) -> None:
#         self.nome = nome
#         self.livros: list[Livro] = []
    
#     def adicionar_livro(self, livro: Livro) -> None:
#         self.livros.append(livro)
    
#     def exibir_livro(self) -> None:
#         for livro in self.livros:
#              print(f"Título: {livro.titulo} -- Autor: {livro.autor}")

# li = Livro("Dom Casmurro", "Machado de Assis")
# li2 = Livro("Memórias Póstumas", "Machado de Assis")
# bi = Biblioteca("Biblioteca")
# bi.adicionar_livro(li)
# bi.adicionar_livro(li2)
# bi.exibir_livro()

# # Exercício 03 - Aula 03: Composição
# class Endereco:
#     def __init__(self, rua: str, cidade: str) -> None:
#         self.rua = rua
#         self.cidade = cidade

#     def obter_formatado(self) -> str:
#         return f"{self.rua}, {self.cidade}"

# class Pessoa:
#     def __init__(self, nome: str, rua: str, cidade: str) -> None:
#         self.nome = nome
#         self.endereco = Endereco(rua, cidade)

#     def exibir_dados(self) -> None:
#         print(f"Nome: {self.nome}")
#         print(f"Endereço: {self.endereco.obter_formatado()}")

# p = Pessoa("João", "Rua Vinte e Cinco de Março", "São Paulo")
# p.exibir_dados()

# # Exercício 04 - Aula 04: Associação, Agregação e Composição
# class Projetor:
#     def __init__(self, nome_aula: str) -> None:
#         self.nome_aula = nome_aula

#     def exibir_slides(self) -> None:
#         print(f"Exibindo slides da aula de {self.nome_aula}...")

# class Professor:
#     def __init__(self, nome: str) -> None:
#         self.nome = nome

#     def dar_aula(self, projetor: Projetor) -> None:
#         projetor.exibir_slides()

# class GradeCurricular:
#     def __init__(self, nome_curso: str) -> None:
#         self.nome_curso = nome_curso

#     def detalhar(self) -> None:
#         print(f"Nome do curso: {self.nome_curso}")

# class Universidade:
#     def __init__(self, nome: str, grade_curricular: str):
#         self.nome = nome
#         self.grade_curricular = GradeCurricular(grade_curricular)
#         self.lista_professor: list[Professor] = []
    
#     def contratar_professor(self, professor: Professor) -> None:
#         self.lista_professor.append(professor)
#         print(f"O professor {professor.nome} foi contratado.")

#     def exibir_relatorio(self) -> None:
#         print("=== Relatório da Universidade ===")
#         print(f"Nome da Universidade: {self.nome}")
#         print(f"Grade Curricular: {self.grade_curricular.nome_curso}")
#         for professor in self.lista_professor:
#             print(professor.nome)

# p1 = Projetor("Programação Orientada a Objetos")
# p1.exibir_slides()
# p2 = Professor("Higor")
# g = GradeCurricular("Sistemas para Internet")
# u = Universidade("Universidade Federal Fluminense", "Sistemas para Internet")
# u.contratar_professor(p2)
# u.exibir_relatorio()

# # Exercicio 05 - Aula 05: Herança
# class Veiculo:
#     def __init__(self, marca: str, modelo: str) -> None:
#         self.marca = marca
#         self.modelo = modelo

#     def acelerar(self) -> None:
#         print("Veículo acelerando...")

# class Carro(Veiculo):
#     def __init__(self, marca: str, modelo: str, qtd_portas: int) -> None:
#         super().__init__(marca, modelo)
#         self.qtd_portas = qtd_portas

#     def acelerar(self) -> None:
#         print(f"Carro {self.marca} {self.modelo} acelerando com {self.qtd_portas} portas!")

# class Moto(Veiculo):
#     def __init__(self, marca: str, modelo: str) -> None:
#         super().__init__(marca, modelo)

#     def acelerar(self) -> None:
#         print(f"Moto {self.marca} {self.modelo} acelerando!")

# c = Carro("XYZ", "Hibrido", 6)
# c.acelerar()
# m = Moto("XYZ", "Veloz")
# m.acelerar()

# # Exercicio 06 - Aula 06: Herança Múltipla e MRO
# class Documento:
#     def __init__(self, titulo: str, conteudo: str) -> None:
#         self.titulo = titulo
#         self.conteudo = conteudo

# class ExportavelJSONMixin:
#     def para_json(self) -> str:
#         return f'{{"titulo": "{self.titulo}", "conteudo": "{self.conteudo}"}}'

# class RelatorioFinanceiro(Documento, ExportavelJSONMixin):
#     def __init__(self, titulo: str, conteudo: str, valor_total: float) -> None:
#         super().__init__(titulo, conteudo)
#         self.valor_total = valor_total

# r = RelatorioFinanceiro("Balanço Q3", "Lucro líquido elevado", 150000.0)
# print(r.para_json())

# Exercicio Desafio 01 - Bloco 01 e Bloco 02:

class NotificavelMixin:
    def notificar(self, mensagem: str) -> None:
        print(f"[NOTIFICAÇÃO]: {mensagem}")

class Veiculo:
    def __init__(self, placa: str, capacidade_carga: float) -> None:
        self.placa = placa
        self.capacidade_carga = capacidade_carga

    def calcular_custo_viagem(self, distancia_km: float) -> float:
        return distancia_km * 2.0

class Caminhao(Veiculo):
    def __init__(self, placa: str, capacidade_carga: float, qtd_eixos: int) -> None:
        super().__init__(placa, capacidade_carga)
        self.qtd_eixos = qtd_eixos

    def calcular_custo_viagem(self, distancia_km: float) -> float:
        return distancia_km * 2.0 + self.qtd_eixos * 50

class Motorista:
    def __init__(self, nome: str, cnh: str) -> None:
        self.nome = nome
        self.cnh = cnh

class Rota:
    def __init__(self, origem: str, destino: str, distancia_km: float) -> None:
        self.origem = origem
        self.destino = destino
        self.distancia_km = distancia_km

    def detalhar(self) -> str:
        return f"{self.origem} -> {self.destino}: {self.distancia_km} km"

class GPS:
    def calcular_tempo(self, distancia_km: float) -> None:
        print(f"[GPS]: Tempo estimado para {distancia_km} km é de {distancia_km/60:.1f} horas.")

class Viagem(NotificavelMixin):
    def __init__(self, origem: str, destino: str, 
    distancia_km: float, veiculo: Veiculo, motorista: Motorista) -> None:
        self.origem = origem
        self.destino = destino
        self.distancia_km = distancia_km
        self.veiculo = veiculo
        self.motorista = motorista
        self.rota = Rota(origem, destino, distancia_km)

    def iniciar_viagem(self, gps: GPS) -> None:
        gps.calcular_tempo(self.rota.distancia_km)
        self.notificar(f"A viagem do motorista {self.motorista.nome} com o veículo de placa {self.veiculo.placa} começou.")

    def resumo(self) -> None:
        print(f"Motorista: {self.motorista.nome}")
        print(f"Placa: {self.veiculo.placa}")
        print(f"Rota detalhada: {self.rota.detalhar()}")
        print(f"Custo total da viagem: {self.veiculo.calcular_custo_viagem(self.distancia_km)}")

m = Motorista("Carlos","ABC1234")
c = Caminhao("XYZ1234", 15000.0, 4)
g = GPS()
v = Viagem("Rio de Janeiro", "Brasilia", 430.0, c, m)
v.iniciar_viagem(g)
v.resumo()