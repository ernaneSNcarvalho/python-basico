lista = [1, 2, 3, 4, 5, 6]

menor = lista[0]
maior = lista[0]

for i in lista:
    if i < menor:
        menor = i
    if i > maior:
        maior = i

print(f"{menor} = menor | {maior} = maior")
