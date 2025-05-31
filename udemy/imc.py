"""
Tabela IMC:
FORMULA: PESO / (ALTURA * ALTURA)
Abaixo de 19.1 - abaixo do peso
Entre 19.1 e 25.8 - Peso normal
Entre 25.9 e 27.3 - Pouco acima do peso
Entre 27.4 e 32.3 - Acima do peso
Acima de 32.4 - Obesidade
"""


def imc(peso, altura):
    res = peso / (altura * altura)
    if res < 19.1:
        return print("Abaixo do peso")
    elif res < 25.8:
        return print("Peso normal")
    elif res <= 27.3:
        return print("Pouco acimm do peso")
    elif res <= 32.3:
        return print("Acima do peso")
    else:
        return print("Obesidade")


altura = float(input("Digite a altura: "))
peso = float(input("Digite o peso: "))

imc(peso, altura)
