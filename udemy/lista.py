lista = ["Banana", "Maçã", "Uva", "Pera", "Jaboticaba"]
print(lista)

print("-------------------------")

removido = input("Digite o item a ser removido: ")

while removido not in lista:
    print("Fruta nao pertence a lista.")
    removido = input("Digite o item a ser removido: ")

for fruta in lista:

    if fruta == removido:
        lista.remove(fruta)

print("-------------------------")
print(lista)
