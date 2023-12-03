from entities import *
from gui import *
import TKinterModernThemes as TKMT
from functools import partial
import tkinter as tk
import json

# # Cria GUI do app
# window = make_window()

# while True:  # Event Loop
#     event, values = window.read()
#     print(event, values)
#     if event == sg.WIN_CLOSED or event == "Sair":
#         break
#     elif event == "Show":
#         # Update the "output" text element to be the value of "input" element
#         window["-OUTPUT-"].update(values["-IN-"])
#     elif event == "Selecionar":
#         print("[LOG] Selecionar pressionado!")
#         if values["-OPTION MENU-"] == "":
#             pass
#         elif values["-OPTION MENU-"] == "Aluno":
#             pass
#         elif values["-OPTION MENU-"] == "Motorista":
#             pass
#         # Update the "output" text element to be the value of "input" element
#         # window["-OUTPUT-"].update(values["-IN-"])

# window.close()

import TKinterModernThemes as TKMT


def buttonCMD():
    print("Button clicked!")


class App(TKMT.ThemedTKinterFrame):
    def __init__(self):
        super().__init__("TITLE", "park", "dark")
        self.button_frame = self.addLabelFrame("Frame Label")
        self.button_frame.Button(
            "Button Text", buttonCMD
        )  # the button is dropped straight into the frame
        self.run()


App()
