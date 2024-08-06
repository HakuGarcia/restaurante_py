from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

# ---
restaurante01 = Restaurante("Pastel da Pam", "Pastel")

bebida01 = Bebida("Caldo de Cana", 5.0, 500)
restaurante01.add_no_cardapio(bebida01)

prato01 = Prato("Pastel de Calabresa", 15.0, "Pastel de calabresa com queijo")
restaurante01.add_no_cardapio(prato01)
# ---

# ---
restaurante02 = Restaurante("Fabricia Doces", "Doces")
# ---

# ---
restaurante03 = Restaurante("Praça Italiana", "Italiana")
# ---

# ---
restaurante04 = Restaurante("Pizza Place", "Pizza")

bebida04 = Bebida("Pepsi", 7.0, 200)
bebida04.aplicar_desconto()
restaurante04.add_no_cardapio(bebida04)

prato04 = Prato("Pizza Baiana", 41.0, "Pizza de calabresa, ovo, pimenta e cebola")
prato04.aplicar_desconto()
restaurante04.add_no_cardapio(prato04)
# ---

# ---
restaurante05 = Restaurante("El Aguacate", "Mexicana")
# ---

def main():
    print("\n - ")
    restaurante01.exibir_cardapio
    print("\n")
    restaurante04.exibir_cardapio
    print(" - \n")
    # print("\n - ")
    # Restaurante.listar()
    # print(" - \n")

if __name__ == '__main__':
    main()