class Configs:
    """
    Classe que contem alguns parâmetros para configuração do app
    """

    def __init__(
        self,
        screenWidth: int,
        screenHeight: int,
        appearance_mode: str,
        theme_color: str,
        wResize: bool,
        hResize: bool,
        logo_path: str = "./assets/logo.png",
        aluno_path: str = "./assets/aluno.png",
        motorista_path: str = "./assets/motorista.png",
    ):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.appearance_mode = appearance_mode
        self.theme_color = theme_color
        self.wResize = wResize
        self.hResize = hResize
        self.logo_path = logo_path
        self.aluno_path = aluno_path
        self.motorista_path = motorista_path
