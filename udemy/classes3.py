class Pessoa: 
    atributo = 'valor'
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def get_ano_nascimento(self):
        return 2025 - self.idade
    
p1 = Pessoa('Joao', 35)
p2 = Pessoa('Helena', 12)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
        
        
