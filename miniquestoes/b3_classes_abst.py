from abc import ABC, abstractmethod
# Exercicio 09 - Aula 09: Classes e Métodos Abstratos
class Forma(ABC):
    @abstractmethod
    def calcular_area(self) -> float:
        """As subclasses irão implementar o método."""

class Quadrado(Forma):
    def __init__(self, lado: float) -> None:
        self.lado = lado

    def calcular_area(self) -> float:
        return self.lado * self.lado

class Circulo(Forma):
    def __init__(self, raio: float) -> None:
        self.raio = raio

    def calcular_area(self) -> float:
        return 3.14 * (self.raio ** 2)

q = Quadrado(3)
c = Circulo(2)
print(q.calcular_area())
print(c.calcular_area())