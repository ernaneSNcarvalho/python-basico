lista = []


def exibir():
    with open("lista.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        for arq in arquivo:
            if len(linhas) == 0:
                print("Arquivo vazio!")
            else:
                for linha in linhas:
                    print(linha.strip())


def adicionar():
    with open("lista.txt", "a") as arquivo:
        quantidade = int(
            input("Qual a quantidade de itens a serem adicionados no carrinho: ")
        )

        for i in range(quantidade):
            item = input("Digite o item: ")
            lista.append(item)
            arquivo.writelines(lista)


opcao = input("[e] - exibir | [a] - adicionar | [s] - sair => ")

while opcao.lower() != "e" and opcao.lower() != "a" and opcao.lower() != "s":
    print("Digite uma opção válida!")
    opcao = input("[e] - exibir | [a] - adicionar | [s] - sair => ")

while opcao.lower() != "s":
    if opcao == "e":
        exibir()
    elif opcao == "a":
        adicionar()
    print("-----------------------------------------")
    opcao = input("[e] - exibir | [a] - adicionar | [s] - sair")
