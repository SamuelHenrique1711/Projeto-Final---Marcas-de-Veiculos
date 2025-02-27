class Carro:
    def __init__(self, nome):
        self.nome = nome
        self.modificacao = None  # A modificação é uma informação interna, não acessada diretamente.

    def customizar(self):
        pass  # Esta função será sobrescrita nas subclasses
