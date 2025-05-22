sair = ""

while sair != "s":
    print("Bem vindo a Calculadora! ")
    try:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
    except ValueError:
        print("Digite somente números!")

    opcao = input(
        "[+]Somar | [-]Subtrair | [*]Multiplicar | [/]Dividir | [s]Sair do Programa =>"
    )

    match opcao:
        case "+":
            print(n1 + n2)
        case "-":
            print(n1 - n2)
        case "*":
            print(n1 * n2)
        case "/":
            print(n1 / n2)
        case "s":
            sair = "s"
        case _:
            print("Opção inválida.")


print("END OF PROGRAM!")
