import re


class Pessoa:
    def __init__(self, nome, idade, email, senha):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.senha = senha

    def email_valido(self):
        # Verifica se tem "@" e "." no email (bem simples)
        return "@" in self.email and "." in self.email

    def senha_valida(self):
        # Verifica se a senha tem pelo menos 4 caracteres
        return len(self.senha) >= 4

    def exibir_dados(self):
        print(f"Nome: {self.nome} | Idade: {self.idade} | E-mail: {self.email}")


pessoas = []
quantidade = int(input("Quantidade de pessoas: "))

for i in range(quantidade):
    print(f"\nPessoa {i + 1}")

    nome = input("Nome: ")
    idade = int(input("Idade: "))

    while True:
        email = input("Email: ")
        senha = input("Senha (mínimo 4 caracteres): ")

        pessoa = Pessoa(nome, idade, email, senha)

        if not pessoa.email_valido():
            print("⚠️  E-mail inválido (deve conter '@' e '.').")
        elif not pessoa.senha_valida():
            print("⚠️  Senha inválida (mínimo 4 caracteres).")
        else:
            break  # Sai do loop se os dois forem válidos

    pessoas.append(pessoa)
    print("✅ Pessoa cadastrada com sucesso.")

# Exibir todos os cadastrados
print("\n--- Pessoas Cadastradas ---")
for p in pessoas:
    p.exibir_dados()
