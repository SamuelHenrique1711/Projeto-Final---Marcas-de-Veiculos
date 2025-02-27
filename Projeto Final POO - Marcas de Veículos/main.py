from bmw import BMW
from mustang import Mustang
from porsche import Porsche

def main():
    # Exibe o título da loja
    print("-----Loja de Carros do Samuel Henrique-------")
    
    marcas = [BMW(), Mustang(), Porsche()]
    
    print("\nSeja Bem-Vindo a nossa loja, temos 3 marcas disponíveis\nPor favor, pode escolher a marca do seu novo carro:")
    for i, marca in enumerate(marcas, start=1):
        print(f"{i}. {marca.nome}")
    
    escolha_marca = int(input("Escolha a marca do carro (1, 2 ou 3): ")) - 1
    if 0 <= escolha_marca < len(marcas):
        marca_escolhida = marcas[escolha_marca]
        carro_escolhido = marca_escolhida.escolher_carro()
        
        if carro_escolhido:
            carro_com_customizacao = marca_escolhida.customizar_carro(carro_escolhido)
            if carro_com_customizacao and carro_com_customizacao.modificacao:
                print(f"\nAqui está a chave do seu carro {carro_com_customizacao.nome}.")
                print(f"Seu carro foi modificado com: {carro_com_customizacao.modificacao}.")
            else:
                print("Desculpe, não foi possível aplicar a customização.")
    else:
        print("Escolha de marca inválida.")

if __name__ == "__main__":
    main()
