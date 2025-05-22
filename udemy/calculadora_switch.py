try:
    n1 = float(input("Primeiro numero: "))
    n2 = float(input("Segundo numero: "))

    opcao = int(input("1 - Somar / 2 - Subtrair / 3 - Multiplicar / 4 - Dividir: "))

    match opcao:
        case 1:
            print(f"A soma de {n1} + {n2} é igual a: {n1 + n2}")
        case 2:
            print(f"A subtração de {n1} - {n2} é igual a: {n1 - n2}")
        case 3:
            print(f"A multiplicação de {n1} x {n2} é igual a: {n1 * n2}")
        case 4:
            print(f"A divisão de {n1} / {n2} é igual a: {n1 / n2}")
except ValueError:
    print("Valor numérico!")
