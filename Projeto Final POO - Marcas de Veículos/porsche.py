from marca_de_veiculos import MarcaDeVeiculos
from carro import Carro

class Porsche(MarcaDeVeiculos):
    def __init__(self):
        super().__init__("Porsche")
        self.adicionar_carro(Carro("Porsche 911"))
        self.adicionar_carro(Carro("Porsche Cayman"))
        self.adicionar_carro(Carro("Porsche Macan"))
    
    def customizar_carro(self, carro):
        print(f"\nOpções de customização para {carro.nome}:")
        print("1. Trocar rodas")
        print("2. Trocar interior")
        escolha = int(input("Escolha a customização (1 ou 2): "))
        if escolha == 1:
            carro.modificacao = "rodas trocadas"
            print(f"Rodas do {carro.nome} foram trocadas.")
        elif escolha == 2:
            carro.modificacao = "interior trocado"
            print(f"Interior do {carro.nome} foi trocado.")
        else:
            print("Opção inválida.")
        return carro
