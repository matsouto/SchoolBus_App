class Rota:
    n_rotas = 0

    def __init__(
        self,
    ):
        self.pontosDeParada = []
        n_rotas = n_rotas + 1
        self.id = n_rotas

    @staticmethod
    def numeroRotas() -> int:
        print(Rota.n_rotas)
        return Rota.n_rotas
