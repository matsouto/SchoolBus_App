from .pessoa import Pessoa
from .pessoaJuridica import Escola
from .contrato import Contrato
from .pontoDeParada import PontoDeParada


class PessoaFisica(Pessoa):
    """Representação de pessoa física. Herda da classe 'Pessoa'"""

    def __init__(
        self,
        nome_oficial: str,
        cpf_cnpj: str,
        telefone: str,
        mae: str,
        pai: str,
        naturalidade: str,
        data_nascimento: str,
        rua: str,
        numero: int,
        complemento: str,
        bairro: str,
    ):
        super().__init__(
            nome_oficial, cpf_cnpj, telefone, rua, numero, complemento, bairro
        )
        self.mae = mae
        self.pai = pai
        self.naturalidade = naturalidade
        self.data_nascimento = data_nascimento

    def apresentarDados(self) -> None:
        super().apresentarDados()
        print(f"Mae: {self.mae}")
        print(f"Pai: {self.pai}")
        print(f"Naturalidade: {self.naturalidade}")
        print(f"Data nascimento: {self.data_nascimento}")

    def getNomeCivil(self) -> str:
        return self.nome_oficial

    def getCPF(self) -> str:
        return self.cpf_cnpj


class Aluno(PessoaFisica):
    def __init__(
        self,
        nome_oficial: str,
        cpf_cnpj: str,
        telefone: str,
        mae: str,
        pai: str,
        naturalidade: str,
        data_nascimento: str,
        matricula: int,
        serie: str,
        escola: Escola,
        pontoDeParada: PontoDeParada,
        rua: str,
        numero: int,
        complemento: str,
        bairro: str,
    ):
        super().__init__(
            nome_oficial,
            cpf_cnpj,
            telefone,
            mae,
            pai,
            naturalidade,
            data_nascimento,
            rua,
            numero,
            complemento,
            bairro,
        )
        self.matricula = matricula
        self.serie = serie
        self.escola = escola
        self.pontoDeParada = pontoDeParada

    def apresentarDados(self) -> None:
        super().apresentarDados()
        print(f"Matricula: {self.matricula}")
        print(f"Serie: {self.serie}")


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
        numero: int,
        complemento: str,
        bairro: str,
        tipo: int,
    ):
        super().__init__(
            nome_oficial,
            cpf_cnpj,
            telefone,
            mae,
            pai,
            naturalidade,
            data_nascimento,
            rua,
            numero,
            complemento,
            bairro,
        )
        self.num_habilitacao = num_habilitacao
        self.cat_habilitacao = cat_habilitacao
        self.tipo = tipo

        # Composição entre Motorista e Contrato
        if self.tipo == 1:
            self.contratos = []

    def apresentarDados(self) -> None:
        super().apresentarDados()
        print(f"Num. habilitação: {self.num_habilitacao}")
        print(f"Cat. habilitação: {self.cat_habilitacao}")
        print(f"Tipo: {self.tipo}")

    def addContrato(self, num_contrato, data_inicio, data_fim, valor) -> bool:
        """Cria um contrato e adiciona à lista"""
        # Verifica se é terceirizado
        if self.tipo == 1:
            _contrato = Contrato(num_contrato, data_inicio, data_fim, valor)
            self.contratos.append(_contrato)
            return True
        else:
            return False

    def eServidor(self) -> bool:
        """Verifica o tipo do motorista"""
        if self.tipo == 0:
            return True
        elif self.tipo == 1:
            return False
