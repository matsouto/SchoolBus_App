import customtkinter
from configs import Configs
from PIL import Image


class Logo(customtkinter.CTkImage):
    def __init__(self, logo_path):
        logo_img_data = Image.open(logo_path)
        super().__init__(
            dark_image=logo_img_data,
            light_image=logo_img_data,
            size=(77.68, 85.42),
        )


class App(customtkinter.CTk):
    def __init__(self, configs: Configs):
        super().__init__()

        self.title("SchoolBus")
        customtkinter.set_appearance_mode(configs.appearance_mode)
        customtkinter.set_default_color_theme(configs.theme_color)

        # Configurações de layout
        self.resizable(configs.wResize, configs.hResize)
        self.geometry(f"{configs.screenWidth}x{configs.screenHeight}")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=10)
        self.grid_rowconfigure(0, weight=1)

        # Cria a sidebar
        self.sidebar_frame = customtkinter.CTkFrame(
            master=self, width=140, corner_radius=10
        )
        self.sidebar_frame.pack_propagate(0)
        self.sidebar_frame.pack(fill="y", anchor="w", side="left")
        self.sidebar_frame.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="nsew")

        # Cria o logo na sidebar
        logo_img_data = Image.open(configs.logo_path)
        logo_img = customtkinter.CTkImage(
            dark_image=logo_img_data,
            light_image=logo_img_data,
            size=(107.68, 115.42),
        )
        self.logo = customtkinter.CTkLabel(
            master=self.sidebar_frame, text="", image=logo_img
        ).pack(pady=(38, 0), anchor="center")

        aluno_img_data = Image.open(configs.aluno_path)
        aluno_img = customtkinter.CTkImage(
            dark_image=aluno_img_data,
            light_image=aluno_img_data,
        )

        self.alunosButton = customtkinter.CTkButton(
            master=self.sidebar_frame,
            image=aluno_img,
            text="Alunos",
            fg_color="transparent",
            font=("Arial Bold", 14),
            hover_color="#207244",
            anchor="w",
        ).pack(anchor="center", ipady=5, pady=(60, 0))

        motorista_img_data = Image.open(configs.motorista_path)
        motorista_img = customtkinter.CTkImage(
            dark_image=motorista_img_data,
            light_image=motorista_img_data,
        )

        self.motoristaButton = customtkinter.CTkButton(
            master=self.sidebar_frame,
            image=motorista_img,
            text="Motoristas",
            fg_color="#fff",
            font=("Arial Bold", 14),
            text_color="#2A8C55",
            hover_color="#eee",
            anchor="w",
        ).pack(anchor="center", ipady=5, pady=(16, 0))

        # tabview = customtkinter.CTkTabview(master=self)
        # tabview.pack(padx=20, pady=20)
        # tabview.add("tab1")
        # tabview.add("tab2")

        # Cria o botão
        # buttom = customtkinter.CTkButton(master=self.sidebar_frame, text="button")
        # # Configura o formato do botão
        # buttom.grid(row=0, column=1, padx=20, pady=20)

        # buttom2 = customtkinter.CTkButton(master=self, text="button")
        # # Configura o formato do botão
        # buttom2.grid(row=1, column=1, padx=20, pady=20)

    def button_callback(self):
        print("button pressed")


if __name__ == "__main__":
    configs = Configs(620, 520, "light", "green", wResize=False, hResize=False)
    app = App(configs=configs)
    app.mainloop()
