class Contrato:
    def __init__(
        self, num_contrato: int, data_inicio: str, data_fim: str, valor: float
    ):
        self.num_contrato = num_contrato
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.valor = valor
