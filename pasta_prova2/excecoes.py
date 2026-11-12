class AgendaError(Exception):
    """A classe AgendaError será usada por meio de raise dentro dos métodos."""

class HorarioIndisponivelError(AgendaError):
    """A classe HorarioIndisponivelError será usada por meio de raise dentro dos métodos."""

class PacienteJaAgendadoError(AgendaError):
    """A classe PacienteJaAgendadoError será usada por meio de raise dentro dos métodos."""