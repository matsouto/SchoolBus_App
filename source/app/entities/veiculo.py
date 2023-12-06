from entities import Contrato


class Veiculo:
    """
    Classe abstrata para veículos
    """

    def __init__(
        self,
        placa: str,
        ano: int,
        modelo: str,
        capacidade: int,
        tipo: int,
        num_contrato: int,
        data_inicio: str,
        data_fim: str,
        valor: float,
    ):
        self.placa = placa
        self.capacidade = capacidade
        self.ano = ano
        self.capacidade = capacidade
        self.tipo = tipo
        self.modelo = modelo
        # Composição entre veículo e contrato
        self.contrato = Contrato(num_contrato, data_inicio, data_fim, valor)

    def verificarTipo(self) -> str:
        """Verifica o tipo do veículo"""
        if self.tipo == 0:
            return "Próprio"
        elif self.tipo == 1:
            return "Alugado"
