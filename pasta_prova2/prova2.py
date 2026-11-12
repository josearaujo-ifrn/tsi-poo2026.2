from dataclasses import dataclass
from abc import ABC, abstractmethod

class AgendaError(Exception):
    """A classe AgendaError será usada por meio de raise dentro dos métodos."""

class HorarioIndisponivelError(AgendaError):
    """A classe AgendaError será usada por meio de raise dentro dos métodos."""

class PacienteJaAgendadoError(AgendaError):
    """A classe AgendaError será usada por meio de raise dentro dos métodos."""

@dataclass
class Paciente:
    nome: str
    cartao_sus: str

class Atendimento(ABC):
    def __init__(self, paciente: Paciente, tipo: str) -> None:
        self.paciente = paciente
        self.tipo = tipo

    @abstractmethod
    def duracao_minutos(self) -> int:
        """As subclasses irão implementar o método"""

class Consulta(Atendimento):
    def __init__(self, paciente, tipo, especialidade: str, retorno: bool = False) -> None:
        super().__init__(paciente, tipo)
        self.especialidade = especialidade
        self.retorno = retorno
    
    def duracao_minutos(self):
        return super().duracao_minutos()

class Exame(Atendimento):
    def __init__(self, paciente, tipo, jejum: bool = False) -> None:
        super().__init__(paciente, tipo)
        self.jejum = jejum
        
    def duracao_minutos(self):
        return super().duracao_minutos()

class Vacinacao(Atendimento):
    def __init__(self, paciente, tipo, vacina: str, doses: int = 1) -> None:
        super().__init__(paciente, tipo)
        self.vacina = vacina
        self.doses = doses
    
    def duracao_minutos(self):
        return super().duracao_minutos()

class Agenda:
    def __init__(self, limite_minutos: int = 240) -> None:
        self.limite_minutos = limite_minutos
        self._lista_atendimentos: list[Atendimento] = []

    @property
    def lista_atendimentos(self) -> list: # verificar dps
        return tuple(self._lista_atendimentos)

    @property
    def minutos_ocupados(self) -> int:
        pass