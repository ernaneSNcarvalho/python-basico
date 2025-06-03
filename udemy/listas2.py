from collections import Counter

lista = [1, 2, 2, 3, 4, 5, 6, 6, 6, 7, 7, 8, 9, 9, 9, 9, 9, 9]
dicionario = Counter(lista)

for item, quantidade in dicionario.items():
    print(f"{item} se repete {quantidade}x")
