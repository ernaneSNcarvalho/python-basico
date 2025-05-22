import random

numero = random.randint(1, 10)
num_dig = int(input("Digite o numero: "))
while numero != num_dig:
    print("Errado!")
    num_dig = int(input("Digite o numero: "))

print("Acertou!")


# numero = random.random()
# print(numero)  # Exemplo: 0.548723

# numero = random.uniform(1.5, 5.5)  # Número como 3.141592
# print(numero)

# frutas = ["maçã", "banana", "laranja", "uva"]
# escolhida = random.choice(frutas)
# print(escolhida)  # Exemplo: "banana"

# cartas = ["Ás", "Rei", "Dama", "Valete"]
# random.shuffle(cartas)
# print(cartas)  # Exemplo: ["Dama", "Ás", "Valete", "Rei"]
