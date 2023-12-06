from .pessoa import Pessoa
from .contrato import Contrato


class PessoaJuridica(Pessoa):
    """
    Representação de pessoa juridica. Herda da classe 'Pessoa'.
    """

    def __init__(
        self,
        nome_oficial: str,
        cpf_cnpj: str,
        telefone: str,
        nome_fantasia: str,
        num_funcionario: int,
        rua: str,
        numero: int,
        complemento: str,
        bairro: str,
    ):
        super().__init__(
            nome_oficial, cpf_cnpj, telefone, rua, numero, complemento, bairro
        )
        self.nome_fantasia = nome_fantasia
        self.num_funcionario = num_funcionario

    def apresentarDados(self) -> None:
        super().apresentarDados()
        print(f"Nome fantasia: {self.nome_fantasia}")
        print(f"Numero do funcionario: {self.num_funcionario}")

    def getNomeFantasia(self) -> str:
        return self.nome_fantasia

    def getCnpj(self) -> str:
        return self.cpf_cnpj


class Fornecedor(PessoaJuridica):
    """
    Representação de fornecedor. Herda da classe 'PessoaJuridica'.
    """

    def __init__(
        self,
        nome_oficial: str,
        cpf_cnpj: str,
        telefone: str,
        nome_fantasia: str,
        num_funcionario: int,
        rua: str,
        numero: int,
        complemento: str,
        bairro: str,
    ):
        super().__init__(
            nome_oficial,
            cpf_cnpj,
            telefone,
            nome_fantasia,
            num_funcionario,
            rua,
            numero,
            complemento,
            bairro,
        )
        self.contratos = []

    def apresentarDados(self) -> None:
        super().apresentarDados()

    def adicionarContrato(self, contrato: Contrato) -> None:
        """
        Adiciona um contrato à lista de contratos do funcionário
        """
        self.contratos.append(contrato)


class Escola(PessoaJuridica):
    def __init__(
        self,
        nome_oficial: str,
        cpf_cnpj: str,
        telefone: str,
        nome_fantasia: str,
        num_funcionario: int,
        rua: str,
        numero: int,
        complemento: str,
        bairro: str,
    ):
        super().__init__(
            nome_oficial,
            cpf_cnpj,
            telefone,
            nome_fantasia,
            num_funcionario,
            rua,
            numero,
            complemento,
            bairro,
        )

        # Relação de agregação entre escola e aluno
        self.alunos = []

    def apresentarDados(self) -> None:
        super().apresentarDados()

    def addAluno(self, aluno) -> None:
        """Adicionar aluno à escola"""
        self.alunos.append(aluno)

    def exibirAlunos(self) -> None:
        """Exibir todos os alunos matriculados"""
        for aluno in self.alunos:
            print()
            print(f"Matricula: {aluno.matricula}")
            print(f"Cpf: {aluno.cpf_cnpj}")
            print(f"Nome: {aluno.nome_oficial}")
            print(f"Serie: {aluno.serie}")
            print()
