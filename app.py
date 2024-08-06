import os

restaurantes = [{"Nome":"Churros da Pam", "Categoria":"Doces", "Ativo":False}, 
                {"Nome":"Fabricia Doces", "Categoria":"Doces", "Ativo":True},
    ]

def menu():
    menu = """
    - 𝕤𝕒𝕓𝕠𝕣 𝕖𝕩𝕡𝕣𝕖𝕤𝕤 -

    1. Cadastrar restaurante
    2. Listar restaurante
    3. Ativar restaurante
    4. Sair
    """
    print(menu)

def voltar():
    input("\nDigite uma tecla para voltar ao menu principal: ")
    main()

def exibir_subtitulo(texto):
    os.system("cls")
    linha = "-" * (len(texto) + 2)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastro_restaurante():
    exibir_subtitulo(" - Cadastro de restaurantes: - ")

    nome_rest = input("Informe o nome do restaurante: ")
    categoria_rest = input(f"Informe a categoria do restaurante {nome_rest}: ")
    dados_rest = {"Nome":nome_rest, "Categoria":categoria_rest, "Ativo":False}
    restaurantes.append(dados_rest)
    
    print(f"O restaurante {nome_rest} foi cadastrado.")
    voltar()
    
def lista_restaurantes():
    exibir_subtitulo(" - Restaurantes cadastrados: - ")

    print(f"  {'Nome:'.ljust(20)} | {'Categoria:'.ljust(15)} | Status:")
    for restaurante in restaurantes:
        ativo = "Ativado" if restaurante['Ativo'] else "Desativado"
        print(f"> {restaurante['Nome'].ljust(20)} | {restaurante['Categoria'].ljust(15)} | {ativo}")

    voltar()

def ativando_restaurante():
    exibir_subtitulo(" - Alteração do restaurante: - ")

    nome_rest = input("Informe o nome do restaurante: ")
    rest_encontrado = False

    for restaurante in restaurantes:
        if nome_rest == restaurante['Nome']:
            rest_encontrado = True
            restaurante['Ativo'] = not restaurante['Ativo']
            msg = f"O restaurante {nome_rest} foi ativado com sucesso!!" if restaurante['Ativo'] else f"O restaurante {nome_rest} foi desativado com sucesso!!"
            print(msg)
    if not rest_encontrado:
        print("O restaurante não foi encontrado.")

    voltar()

def finalizar():
    os.system("cls")
    exibir_subtitulo("Obrigado por usar nosso app!!")

def invalida():
    print("Opção inválida!!")
    voltar()

def opcao():
    try:
        opcao = int(input("Escolha uma opção: "))
        print(f"Você escolheu a opção {opcao}")

        match opcao:
            case 1:
                cadastro_restaurante()
            case 2:
                lista_restaurantes()
            case 3:
                ativando_restaurante()
            case 4:
                finalizar()
            case _:
                invalida()
    except: 
        invalida()

def main():
    os.system("cls")
    menu()
    opcao()

if __name__ == '__main__':
    main()