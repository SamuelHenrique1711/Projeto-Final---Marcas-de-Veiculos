from marca_de_veiculos import MarcaDeVeiculos
from carro import Carro

class BMW(MarcaDeVeiculos):
    def __init__(self):
        super().__init__("BMW")
        self.adicionar_carro(Carro("BMW Série 3"))
        self.adicionar_carro(Carro("BMW X5"))
        self.adicionar_carro(Carro("BMW M4"))
    
    def customizar_carro(self, carro):
        print(f"\nOpções de customização para {carro.nome}:")
        print("1. Trocar capô")
        print("2. Trocar rodas")
        escolha = int(input("Escolha a customização (1 ou 2): "))
        if escolha == 1:
            carro.modificacao = "capô trocado"
            print(f"Capô do {carro.nome} foi trocado.")
        elif escolha == 2:
            carro.modificacao = "rodas trocadas"
            print(f"Rodas do {carro.nome} foram trocadas.")
        else:
            print("Opção inválida.")
        return carro
