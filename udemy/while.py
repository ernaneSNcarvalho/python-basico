maior = 0
menor = 0

num = int(input("Digite o número: "))

numeros = []

while num != 0:
    numeros.append(num)
    num = int(input("Digite o número: "))
    if num > maior:
        maior = num
    else:
        menor = num

print(f"{maior} é o maior")
print(f"{menor} é o menor")
