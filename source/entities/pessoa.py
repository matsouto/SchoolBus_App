from .endereco import Endereco
from .contrato import Contrato


class Pessoa:
    """
    Representação de pessoa
    """

    def __init__(
        self,
        nome_oficial: str,
        endereco: Endereco,
        cpf_cnpj: str,
        telefone: str,
    ):
        self.nome_oficial = nome_oficial
        self.cpf_cnpj = cpf_cnpj
        self.endereco = endereco
        self.telefone = telefone

    def getNomeOficial(self) -> str:
        return self.nome_oficial

    def getCPFCNPJ(self):
        return self.cpf_cnpj


class PessoaFisica(Pessoa):
    """
    Representação de pessoa física. Herda da classe 'Pessoa'.
    """

    def __init__(
        self,
        nome_oficial: str,
        endereco: Endereco,
        cpf_cnpj: str,
        telefone: str,
        mae: str,
        pai: str,
        naturalidade: str,
        data_nascimento: str,
    ):
        super().__init__(nome_oficial, endereco, cpf_cnpj, telefone)
        self.mae = (mae,)
        self.pai = (pai,)
        self.naturalidade = (naturalidade,)
        self.data_nascimento = data_nascimento


class PessoaJuridica(Pessoa):
    """
    Representação de pessoa juridica. Herda da classe 'Pessoa'.
    """

    def __init__(
        self,
        nome_oficial: str,
        endereco: Endereco,
        cpf_cnpj: str,
        telefone: str,
        nome_fantasia: str,
        num_funcionario: int,
    ):
        super().__init__(nome_oficial, endereco, cpf_cnpj, telefone)
        self.nome_fantasia = nome_fantasia
        self.num_funcionario = num_funcionario


class Fornecedor(PessoaJuridica):
    """
    Representação de fornecedor. Herda da classe 'PessoaJuridica'.
    """

    def __init__(
        self,
        nome_oficial: str,
        endereco: Endereco,
        cpf_cnpj: str,
        telefone: str,
        nome_fantasia: str,
        num_funcionario: int,
        contratos: list,
    ):
        super().__init__(nome_oficial, endereco, cpf_cnpj, telefone)
        self.nome_fantasia = nome_fantasia
        self.num_funcionario = num_funcionario
        self.contratos = []

    def adicionarContrato(self, contrato: Contrato) -> None:
        """
        Adiciona um contrato à lista de contratos do funcionário
        """
        self.contratos.append(contrato)


class Escola(PessoaJuridica):
    def __init__(
        self,
        nome_oficial: str,
        endereco: Endereco,
        cpf_cnpj: str,
        telefone: str,
        num_funcionario: str,
        nome_fantasia: str = "",
    ):
        super().__init__(nome_oficial, endereco, cpf_cnpj, telefone)
        self.num_funcionario = num_funcionario
        # Tratamento de caso em que o nome_fantasia não é fornecido
        if self.nome_fantasia == "":
            self.nome_fantasia = self.nome_oficial


class Motorista(PessoaFisica):
    def __init__(
        self,
        nome_oficial: str,
        cpf_cnpj: str,
        telefone: str,
        mae: str,
        pai: str,
        naturalidade: str,
        data_nascimento: str,
        num_habilitacao: str,
        cat_habilitacao: str,
        rua: str,
        numero: str,
        complemento: str,
        nome_social: str = "",
    ):
        super().__init__(
            nome_oficial,
            cpf_cnpj,
            telefone,
            mae,
            pai,
            naturalidade,
            data_nascimento,
        )
        # Tratamento caso o nome_social não seja informado
        if self.nome_social == "":
            self.nome_social = self.nome_oficial
        self.num_habilitacao = num_habilitacao
        self.cat_habilitacao = cat_habilitacao
        self.endereco = Endereco(rua, numero, complemento)
