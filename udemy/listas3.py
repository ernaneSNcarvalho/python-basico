from collections import Counter

lista = ["Maca", "Maca", "Banana", "Banana", "Abacaxi", "Abacaxi", "Abacaxi"]
lista.reverse()
dicionario = Counter(lista)

for item, quantidade in dicionario.items():
    print(f"{item} se repete {quantidade}x")

print(lista)
