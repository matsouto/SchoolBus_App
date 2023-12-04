import os
from textual.app import App, ComposeResult
from textual.containers import Container, Center
from textual.widgets import Header, Footer, Button, Static


class mainMenu(Static):
    def compose(self) -> ComposeResult:
        with Center():
            yield Button(
                label="Alunos", id="alunosBtn", variant="warning", disabled=False
            )
            yield Button(
                label="Motoristas",
                id="motoristasBtn",
                variant="warning",
                disabled=False,
            )
            yield Button(
                label="Escolas", id="escolasBtn", variant="warning", disabled=False
            )
            yield Button(
                label="Veículos", id="veiculosBtn", variant="warning", disabled=False
            )
            yield Button(
                label="Rotas", id="rotasBtn", variant="warning", disabled=False
            )


class SchoolBusApp(App):
    """Aplicativo para gestão de ônibus escolar"""

    CSS_PATH = "../style/app.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Cria componentes filhos para o app"""
        yield Header()
        yield mainMenu()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = SchoolBusApp()
    app.run()
