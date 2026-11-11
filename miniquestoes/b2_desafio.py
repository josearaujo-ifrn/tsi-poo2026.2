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