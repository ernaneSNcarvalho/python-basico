'''
class - Classes são moldes para criar objetos 
As classes gram novos objetos (instancias) que, 
podem ter seus proprios atributos e metodos.
Os objetos gerados pela classe podem usar seus dados
internos para realizar varias seções.
Por convenção, usamos PASCALCASE para nomes de classes.
'''

class Pessoa: 
    def __init__ (self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa("Luiz", "Otavio")
p2 = Pessoa('Maria', 'Silva')


print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)