from datetime import date

class Contrato():
    def __init__(self, num_contrato: int, data_inicio: date, data_fim: date, valor: float):
        self.num_contrato = num_contrato
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.valor = valor


