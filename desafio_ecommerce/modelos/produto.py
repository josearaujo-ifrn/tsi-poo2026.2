from abc import ABC, abstractmethod
from datetime import date

class Produto(ABC):
    def __init__(self, nome: str, codigo: str, preco: float, validade: date) -> None:
        self._nome = nome
        self._codigo = codigo
        self._preco = preco
        self._validade = validade

    @property
    def preco(self) -> float:
        return self._preco

    @preco.setter
    def preco(self, preco: float) -> None:
        if preco <= 0:
            raise ValueError("O preço deve ser maior que zero.")
        else:
            self._preco = preco

    @classmethod
    def de_string(cls, texto: str) -> Produto:
        Tipo, Nome, Codigo, Preco, DataValidade, Extras = texto.split(";")
        Validade = date.fromisoformat(DataValidade)
        if Tipo.upper() == "FISICO":
            return ProdutoFisico(Nome, Codigo, Preco, Validade, Extras)
        elif Tipo.upper() == "DIGITAL":
            return ProdutoDigital(Nome, Codigo, Preco, Validade, Extras)
        else:
            raise ValueError(f"O tipo {Tipo} é inválido.")

    @staticmethod
    def calcular_imposto_padrao(valor: float) -> float:
        print(f"O valor {valor} possui imposto de:")
        return valor * 0.10

    def __str__(self) -> str:
        return f"Produto: {self._nome}\nCodigo: {self._codigo}\nPreço: {self._preco}\nValidade: {self._validade}"
    
    def __repr__(self) -> str:
        return f"Produto(nome={self._nome}), Preço(preco={self._preco})"

    def __eq__(self, outro: Produto) -> bool:
        if isinstance(outro, Produto):
            return self._codigo == outro._codigo
        else:
            return False

    def __lt__(self, outro: Produto) -> bool:
        return self._validade < outro._validade

    @abstractmethod
    def calcular_preco_final(self) -> float:
        """As subclasses irão implementar o método."""

class ProdutoFisico(Produto):
    def __init__(self, nome, codigo, preco, validade, peso_kg: float) -> None:
        super().__init__(nome, codigo, preco, validade)
        self.peso_kg = peso_kg

    def calcular_preco_final(self) -> float:
        frete = self.peso_kg * 5.0
        return self.preco + frete

class ProdutoDigital(Produto):
    def __init__(self, nome, codigo, preco, validade, tamanho_mb: float) -> None:
        super().__init__(nome, codigo, preco, validade)
        self.tamanho_mb = tamanho_mb

    def calcular_preco_final(self):
        return self.preco