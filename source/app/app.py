import os
import json
from rich import print as rprint
from rich.console import Console
from rich.table import Table
from textual.app import App, ComposeResult
from textual.containers import Container, ScrollableContainer, Center
from textual.widgets import Header, Footer, Button, Static, Label

import entities


class mainMenu(App):
    """Menu inicial da aplicação"""

    CSS_PATH = "../style/app.tcss"
    BINDINGS = [("escape", "request_quit", "Sair")]

    def action_request_quit(self) -> None:
        self.app.exit()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Callback dos botões"""
        global menu_option  # Permite enviar de volta o valor selecionado antes do exit()
        if event.button.id == "alunosBtn":
            menu_option = "alunos"
            self.app.exit()
        elif event.button.id == "motoristasBtn":
            menu_option = "motoristas"
            self.app.exit()

    def compose(self) -> ComposeResult:
        """Cria componentes filhos para o app"""
        yield Header()
        yield Container(
            Center(
                Button(
                    label="Alunos", id="alunosBtn", variant="primary", disabled=False
                )
            ),
            Center(
                Button(
                    label="Motoristas",
                    id="motoristasBtn",
                    variant="primary",
                    disabled=False,
                )
            ),
            Center(
                Button(
                    label="Escolas", id="escolasBtn", variant="primary", disabled=False
                ),
                Button(
                    label="Veículos",
                    id="veiculosBtn",
                    variant="primary",
                    disabled=False,
                ),
            ),
            Center(
                Button(label="Rotas", id="rotasBtn", variant="primary", disabled=False)
            ),
        )
        yield Footer()


def run_motoristas(motoristasList) -> None:
    """Funcionalidades para interface com o usuário na seção 'Motoristas'"""

    console = Console()

    # Cabeçalho
    console.rule("[bold blue]Motoristas[/bold blue]")
    console.print()

    # Exibe todas os objetos "Motorista" salvos em uma tabela
    # helpers.exibir_tabela(motoristasList, "motoristas")
    console.print()

    # Menu de seleção
    console.print("[bold blue]O que deseja fazer?[/bold blue]")
    console.print()
    console.print("[yellow](1) Verificar[/yellow]", justify="left")
    console.print("[yellow](2) Adicionar[/yellow]", justify="left")
    console.print()

    # Tratamento de entradas
    while True:
        menu_option = int(input())
        if menu_option != 1 and menu_option != 2:
            console.print("[bold red]Entrada não permitida![/bold red]")
            console.print()
        else:
            break

    if menu_option == 1:
        pass

    elif menu_option == 2:
        addMotorista()


def addMotorista() -> entities.Motorista:
    """Interface para criar um objeto motorista"""

    console = Console()

    # Cabeçalho
    console.rule("[bold blue]Adicionar Motorista[/bold blue]")
    console.print()

    # Menu de seleção
    console.print("[bold blue]Digite as informações necessárias:[/bold blue]")
    console.print()

    nome = console.input("[yellow]Nome: [/yellow]")
    cpf = console.input("[yellow]Cpf: [/yellow]")
    telefone = console.input("[yellow]Telefone: [/yellow]")
    mae = console.input("[yellow]Mãe: [/yellow]")
    pai = console.input("[yellow]Pai: [/yellow]")
    naturalidade = console.input("[yellow]Naturalidade: [/yellow]")
    data_nascimento = console.input("[yellow]Data de nascimento: [/yellow]")
    num_habilitacao = console.input("[yellow]Número de habilitação: [/yellow]")
    cat_habilitacao = console.input("[yellow]Categoria de habilitação: [/yellow]")
    rua = console.input("[yellow]Rua: [/yellow]")
    numero = int(console.input("[yellow]Número: [/yellow]"))
    complemento = console.input("[yellow]Complemento: [/yellow]")
    bairro = console.input("[yellow]Bairro: [/yellow]")
    tipo = int(console.input("[yellow]Tipo: [/yellow]"))

    console.print()

    # Cria o objeto
    motorista = entities.Motorista(
        nome,
        cpf,
        telefone,
        mae,
        pai,
        naturalidade,
        data_nascimento,
        num_habilitacao,
        cat_habilitacao,
        rua,
        numero,
        complemento,
        bairro,
        tipo,
    )

    # Conta o número de arquivos para o index
    n_files = 0
    dir_path = "./data/motoristas"
    for path in os.listdir(dir_path):
        # Checa se é arquivo
        if os.path.isfile(os.path.join(dir_path, path)):
            n_files += 1

    # Salva objeto no seu arquivo
    with open(f"./data/motoristas/motorista{n_files}.json", "a") as file:
        json.dump(motorista.__dict__, file, indent=4)

    return motorista


if __name__ == "__main__":
    os.system("clear")
    motoristasList = []

    # Carrega os objetos salvos
    data_path = "./data"
    folder_paths = []
    folder_names = []
    for path in os.listdir(data_path):
        folder_paths.append(os.path.join(data_path, path))
        folder_names.append(path)

    # Para cada pasta criada
    for i, path in enumerate(folder_paths):
        # Se a pasta for "motoristas"
        if folder_names[i] == "motoristas":
            for file in os.listdir(path):
                # Checa se é arquivo
                if os.path.isfile(os.path.join(path, file)):
                    # Lê o arquivo e cria o objeto
                    _dict = json.load(open(os.path.join(path, file)))
                    _motorista = entities.Motorista(
                        nome_oficial=_dict["nome_oficial"],
                        cpf_cnpj=_dict["cpf_cnpj"],
                        telefone=_dict["telefone"],
                        mae=_dict["mae"],
                        pai=_dict["pai"],
                        naturalidade=_dict["naturalidade"],
                        data_nascimento=_dict["data_nascimento"],
                        num_habilitacao=_dict["num_habilitacao"],
                        cat_habilitacao=_dict["cat_habilitacao"],
                        rua=_dict["endereco"]["rua"][0],
                        numero=_dict["endereco"]["numero"][0],
                        complemento=_dict["endereco"]["complemento"][0],
                        bairro=_dict["endereco"]["bairro"][0],
                        tipo=_dict["tipo"],
                    )
                    motoristasList.append(_motorista)

    # Opção escolhida no menu principal
    menu_option = None

    # Inicia o menu principal
    app = mainMenu()
    app.run()

    while True:
        if menu_option == "alunos":
            pass
        elif menu_option == "motoristas":
            _motorista = run_motoristas(motoristasList)
            motoristasList.append(_motorista)
