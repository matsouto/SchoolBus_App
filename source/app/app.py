import os
from textual.app import App, ComposeResult
from textual.containers import Container, Center
from textual.screen import Screen
from textual.widgets import Header, Footer, Button, Static

import customtkinter
import tkinter
from configs import Configs
from helpers import create_class_view
from PIL import Image


class MotoristasView(customtkinter.CTk):
    def __init__(self, configs: Configs):
        super().__init__()

        self.title("Motoristas")
        customtkinter.set_appearance_mode(configs.appearance_mode)
        customtkinter.set_default_color_theme(configs.theme_color)

        # Configurações de layout
        self.resizable(configs.wResize, configs.hResize)
        self.geometry(f"{configs.screenWidth}x{configs.screenHeight}")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Cria a mainView
        self.main_view = customtkinter.CTkFrame(
            master=self, width=140, corner_radius=10
        )
        self.main_view.grid(
            row=0,
            column=0,
            padx=10,
            pady=(10, 10),
            sticky="nsew",
        )
        create_class_view(self, self.main_view, "Motoristas", configs=configs)

    def button_callback(self):
        print("button pressed")


class mainMenu(Static):
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Callback dos botões"""
        if event.button.id == "alunosBtn":
            pass
        elif event.button.id == "motoristasBtn":
            app = MotoristasView(configs=configs)
            app.mainloop()

    def compose(self) -> ComposeResult:
        with Center():
            yield Button(
                label="Alunos", id="alunosBtn", variant="primary", disabled=False
            )
            yield Button(
                label="Motoristas",
                id="motoristasBtn",
                variant="primary",
                disabled=False,
            )
            yield Button(
                label="Escolas", id="escolasBtn", variant="primary", disabled=False
            )
            yield Button(
                label="Veículos", id="veiculosBtn", variant="primary", disabled=False
            )
            yield Button(
                label="Rotas", id="rotasBtn", variant="primary", disabled=False
            )


class SchoolBusApp(App):
    """Aplicativo para gestão de ônibus escolar"""

    CSS_PATH = "../style/app.tcss"
    BINDINGS = [("escape", "request_quit", "Sair")]

    def action_request_quit(self) -> None:
        self.app.exit()

    def compose(self) -> ComposeResult:
        """Cria componentes filhos para o app"""
        yield Header()
        yield mainMenu()
        yield Footer()


if __name__ == "__main__":
    configs = Configs(620, 520, "dark", "dark-blue", wResize=False, hResize=False)
    app = SchoolBusApp()
    app.run()
