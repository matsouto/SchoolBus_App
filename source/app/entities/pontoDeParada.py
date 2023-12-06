class PontoDeParada:
    n_pontos = 0

    def __init__(
        self,
        nome: str,
        latitude: float,
        longitude: float,
    ):
        self.nome = nome
        self.latitude = latitude
        self.longitude = longitude
        self.alunos = []
        n_pontos = n_pontos + 1
        self.id = n_pontos

    @staticmethod
    def numeroRotas() -> int:
        print(PontoDeParada.n_rotas)
        return PontoDeParada.n_rotas
