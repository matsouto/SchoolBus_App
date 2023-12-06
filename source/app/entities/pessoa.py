from .endereco import Endereco
from .contrato import Contrato


class Pessoa:
    """
    Representação de pessoa
    """

    def __init__(
        self,
        nome_oficial: str,
        cpf_cnpj: str,
        telefone: str,
        rua: str,
        numero: int,
        complemento: str,
        bairro: str,
    ):
        self.nome_oficial = nome_oficial
        self.cpf_cnpj = cpf_cnpj
        self.telefone = telefone
        self.endereco = Endereco(rua, numero, complemento, bairro)

    def apresentarDados(self) -> None:
        print(f"Nome oficial: {self.nome_oficial}")
        print(f"Cpf_cnpj: {self.cpf_cnpj}")
        print(f"Telefone: {self.telefone}")
        print(f"Rua: {self.rua}")
        print(f"Numero: {self.numero}")
        print(f"Complemento: {self.complemento}")
        print(f"Bairro: {self.bairro}")

    def verificarTipo(self) -> str:
        """Método polimórfico para verificar a classe do objeto"""
        return type(self)
