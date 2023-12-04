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
    ):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.appearance_mode = appearance_mode
        self.theme_color = theme_color
        self.wResize = wResize
        self.hResize = hResize

        # Icons an logo image paths
        self.logo_path = "./assets/logo.png"
        self.aluno_path = "./assets/aluno.png"
        self.motorista_path = "./assets/motorista.png"
