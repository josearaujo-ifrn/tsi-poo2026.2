from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass(frozen=True)
class Paciente:
    nome: str
    cartao_sus: str

class Atendimento(ABC):
    def __init__(self, paciente: Paciente) -> None:
        self.paciente = paciente

    @abstractmethod
    def duracao_minutos(self) -> int:
        """As subclasses irão implementar o método"""

    def __str__(self):
        return f"Tipo de Atendimento: {self.tipo}\nNome do Paciente:{self.paciente.nome}\nDuração:{self.duracao_minutos()}"

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

    def __str__(self):
        return f"Tipo de Atendimento: Consulta\nNome do Paciente:{self.paciente.nome}\nDuração:{self.duracao_minutos()}"

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

    def __str__(self):
        return f"Tipo de Atendimento: Exame\nNome do Paciente:{self.paciente.nome}\nDuração:{self.duracao_minutos()}"

class Vacinacao(Atendimento):
    def __init__(self, paciente: Paciente, vacina: str, doses: int = 1) -> None:
        super().__init__(paciente)
        self.vacina = vacina
        self.doses = doses
    
    def duracao_minutos(self) -> int:
        return 10

    def __str__(self):
        return f"Tipo de Atendimento: Vacinacao\nNome do Paciente:{self.paciente.nome}\nDuração:{self.duracao_minutos()}"

class Agenda:
    def __init__(self, limite_minutos: int = 240) -> None:
        self.limite_minutos = limite_minutos
        self._lista_atendimentos: any = []

    def agendar(self, tipo: str) -> None:
        print("Digite CONSULTA ou EXAME ou VACINACAO")
        if tipo.upper() == "CONSULTA":
            consulta = Consulta()
            self._lista_atendimentos.append(consulta)
        elif tipo.upper() == "EXAME":
            exame = Exame()
            self._lista_atendimentos.append(exame)
        elif tipo.upper() == "VACINACAO":
            vacinacao = Vacinacao()
            self._lista_atendimentos.append(vacinacao)
        else:
            raise ValueError("Digite o tipo correto.")