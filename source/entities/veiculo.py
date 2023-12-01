from abc import ABC
from .contrato import Contrato


class Veiculo(ABC):
    '''
    Classe abstrata para veículos
    '''
    def __init__(self, placa: str, ano: int, modelo: str, capacidade: int):
        self.placa = placa
        self.capacidade = capacidade
        self.modelo = modelo

class VeiculoAlugado(Veiculo):
    '''
    A classe VeiculoAlugado possui parâmetro adicional 'contrato'.
    '''
    def __init__(self, placa: str, ano: int, modelo: str, capacidade: int, contrato: Contrato):
        super().__init__(placa, ano, modelo, capacidade)
        self.contrato = contrato 

class VeiculoProprio(Veiculo):

    def __init__(self, placa: str, ano: int, modelo: str, capacidade: int):
        super().__init__(placa, ano, modelo, capacidade)
