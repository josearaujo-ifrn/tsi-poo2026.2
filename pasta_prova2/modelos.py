from dataclasses import dataclass
from abc import ABC, abstractmethod
from excecoes import AgendaError, PacienteJaAgendadoError, HorarioIndisponivelError

@dataclass(frozen=True)
class Paciente:
    nome: str
    cartao_sus: str

class Atendimento(ABC):
    def __init__(self, paciente: Paciente) -> None:
        self._paciente = paciente

    @abstractmethod
    def duracao_minutos(self) -> int:
        """As subclasses irão implementar o método"""

    def __str__(self) -> str: # coloquei tipo_subclasse pra cada subclasse falar o tipo de atendimento
        return f"Tipo de Atendimento: 'tipo_subclasse'\nNome do Paciente:{self._paciente.nome}\nDuração:{self.duracao_minutos()}"

class Consulta(Atendimento):
    def __init__(self, paciente: Paciente, especialidade: str, retorno: bool = False) -> None:
        super().__init__(paciente)
        self.especialidade = especialidade
        self.retorno = retorno
    
    def duracao_minutos(self) -> int:
        if self.retorno == True:
            return 15
        else:
            return 30

    def __str__(self) -> str:
        return f"Tipo de Atendimento: Consulta\nNome do Paciente:{self._paciente.nome}\nDuração:{self.duracao_minutos()}"

class Exame(Atendimento):
    def __init__(self, paciente: Paciente, tipo: str, jejum: bool = False) -> None:
        super().__init__(paciente)
        self.tipo = tipo
        self.jejum = jejum
        
    def duracao_minutos(self) -> int:
        if self.jejum == True:
            return 30
        else:
            return 20

    def __str__(self) -> str:
        return f"Tipo de Atendimento: Exame\nNome do Paciente:{self._paciente.nome}\nDuração:{self.duracao_minutos()}"

class Vacinacao(Atendimento):
    def __init__(self, paciente: Paciente, vacina: str, doses: int = 1) -> None:
        super().__init__(paciente)
        self.vacina = vacina
        self.doses = doses
    
    def duracao_minutos(self) -> int:
        return 10

    def __str__(self) -> str:
        return f"Tipo de Atendimento: Vacinacao\nNome do Paciente:{self._paciente.nome}\nDuração:{self.duracao_minutos()}"


class Agenda: # peguei a agenda do commit antigo e mudei o type hint do property 1
    def __init__(self, limite_minutos: int = 240) -> None:
        self.limite_minutos = limite_minutos
        self._lista_atendimentos: list[Consulta | Exame | Vacinacao] = []

    @property
    def lista_atendimentos(self) -> tuple: 
        return tuple(self._lista_atendimentos)

    @property
    def minutos_ocupados(self) -> int:
        pass

    def agendar(self, atendimento: Consulta | Exame | Vacinacao, total: int = 0 ) -> None:
        total = 0
        for item in self._lista_atendimentos:
            total = item.duracao_minutos()
        if total <= self.limite_minutos:
            self._lista_atendimentos = [atendimento]
        else:
            raise HorarioIndisponivelError