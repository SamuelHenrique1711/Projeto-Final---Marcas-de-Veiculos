from marca_de_veiculos import MarcaDeVeiculos
from carro import Carro

class Mustang(MarcaDeVeiculos):
    def __init__(self):
        super().__init__("Mustang")
        self.adicionar_carro(Carro("Mustang GT"))
        self.adicionar_carro(Carro("Mustang Mach 1"))
        self.adicionar_carro(Carro("Mustang Shelby GT500"))
    
    def customizar_carro(self, carro):
        print(f"\nOpções de customização para {carro.nome}:")
        print("1. Trocar aerofólio")
        print("2. Trocar escapamento")
        escolha = int(input("Escolha a customização (1 ou 2): "))
        if escolha == 1:
            carro.modificacao = "aerofólio trocado"
            print(f"Aerofólio do {carro.nome} foi trocado.")
        elif escolha == 2:
            carro.modificacao = "escapamento trocado"
            print(f"Escapamento do {carro.nome} foi trocado.")
        else:
            print("Opção inválida.")
        return carro
