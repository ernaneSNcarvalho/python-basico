def somar(x, y):
    res = x + y
    return res


def subtrair(x, y):
    res = x - y
    return res


def dividir(x, y):
    res = x / y
    return res


def multiplicar(x, y):
    res = x * y
    return res


opcao = input(
    "Digite a opção [s - somar | d - dividir | m - multiplicar | sub - subtrair | x - sair]: "
)

while opcao != "x":

    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    match opcao:
        case "s":
            print(somar(x, y))
        case "d":
            print(dividir(x, y))
        case "m":
            print(multiplicar(x, y))
        case "sub":
            print(subtrair(x, y))
        case _:
            print("Digite uma opção valida!")

    opcao = input(
        "Digite a opção [s - somar | d - dividir | m - multiplicar | sub - subtrair | x - sair]: "
    )
