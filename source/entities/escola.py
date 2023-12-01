from .endereco import Endereco


class Escola:
    def __init__(
        self,
        nome: str,
        cnpj: str,
        telefone: str,
        rua: str,
        numero: int,
        complemento: str,
        bairro: str,
    ):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        # Relação de composição entre escola e endereço
        self.endereco = Endereco(rua, numero, complemento, bairro)
