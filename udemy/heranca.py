class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def oi(self):
        print(f"Oi, meu nome é {self.nome} e tenho {self.idade} anos")


class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def exibir_salario(self):
        print(f"O meu salário é : R$ {self.salario:.2f}")


nome = input("Nome: ")
idade = int(input("Idade: "))
salario = float(input("Salario: "))

funcionario = Funcionario(nome, idade, salario)
funcionario.exibir_salario()
funcionario.oi()  # Ele herdou o metodo de pessoa também
