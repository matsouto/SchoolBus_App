import os
from textual.app import App, ComposeResult
from textual.containers import Container, Center
from textual.screen import Screen
from textual.widgets import Header, Footer, Button, Static


class motoristasScreen(Screen):
    BINDINGS = [("ESC", "app.pop_screen", "Retornar")]

    def compose(self) -> ComposeResult:
        yield Header()
        with Center():
            yield Container(
                Static(" Windows ", id="title"),
                Static("Error"),
                Static("Press any key to continue [blink]_[/]", id="any-key"),
            )
        Footer(),


class mainMenu(Static):
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Callback dos botões"""
        if event.button.id == "alunosBtn":
            pass
        elif event.button.id == "motoristasBtn":
            self.app.push_screen(motoristasScreen())

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
    SCREENS = {"mainMenu": mainMenu(), "motoristasScreen": motoristasScreen()}
    # BINDINGS = [("b", "push_screen('bsod')", "BSOD")]
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
