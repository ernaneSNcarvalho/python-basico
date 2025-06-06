# PROJETO CADASTRO DE CLIENTES
"""
Regras:
- Classe Pessoa(nome, idade)
- Classe Cliente(e-mail e LTV (qtde gasta pelo cliente)) + herança
- Cadastre 2 clientes diferentes em uma lista
- Exiba a lista de todos os clientes cadastrados
- Extra: Exiba a soma de LTV de todos clientes
"""
soma = 0
clientes = []


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def exibir(self):
        print(f"{self.nome} tem {self.idade}")

    def get_nome(self):
        return self._nome

    def get_idade(self):
        return self._idade

    def set_nome(self, novo_nome):
        self._nome = novo_nome

    def set_idade(self, nova_idade):
        self._idade = nova_idade


class Cliente(Pessoa):
    def __init__(self, nome, idade, email, ltv):
        super().__init__(nome, idade)
        self._email = email
        self._ltv = ltv

    def get_email(self):
        return self._email

    def get_ltv(self):
        return self._ltv

    def set_email(self, novo_email):
        self._email = novo_email

    def set_ltv(self, novo_ltv):
        self._ltv = novo_ltv

    def exibir_cliente(self):
        print(
            f"Nome: {self._nome} |Idade: {self._idade} |Email: {self._email} |Ltv: {self._ltv} "
        )


quantidade = int(input("Quantidade de clientes: "))

for i in range(quantidade):
    print(f"Cadastro do {i+1}º cliente: \n")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    email = input("Email: ")
    ltv = float(input("LTV: "))
    clientes.append(Cliente(nome, idade, email, ltv))

for cli in clientes:
    cli.exibir_cliente()

for x in clientes:
    soma += x.get_ltv()

print(f"Soma dos LTVs = R$ {soma:.2f}")
