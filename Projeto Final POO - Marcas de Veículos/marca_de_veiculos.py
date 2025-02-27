class MarcaDeVeiculos:
    def __init__(self, nome):
        self.nome = nome
        self.carros = []
    
    def adicionar_carro(self, carro):
        self.carros.append(carro)
    
    def escolher_carro(self):
        print(f"\nEscolha um carro da marca {self.nome}:")
        for i, carro in enumerate(self.carros, start=1):
            print(f"{i}. {carro.nome}")
        escolha = int(input("Digite o número do carro que você deseja escolher: ")) - 1
        if 0 <= escolha < len(self.carros):
            return self.carros[escolha]
        else:
            print("Escolha inválida.")
            return None
    
    def customizar_carro(self, carro):
        print(f"\nPersonalização disponível para o carro {carro.nome} da marca {self.nome}:")
        return carro.customizar()
