"""
    Fatiamento de strings
    [012345678]
    [Ola mundo] 
    [-987654321]
    Fatiamento [i:f:p] [::]
    Obs: a funcao len retorna a quantidade
    de caracteres da str 
"""

variavel = 'Ola Mundo'
print(variavel[2:3])
print(len(variavel))

nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')
 
if nome and idade:
     print(f'Seu nome é {nome}')
     print(f'Seu nome invertido é {nome[::-1]}')
 
     if ' ' in nome:
         print('Seu nome contém espaços')
     else:
         print('Seu nome NÃO contém espaços')
 
     print(f'Seu nome tem {len(nome)} letras')
     print(f'A primeira letra do seu nome é {nome[0]}')
     print(f'A última letra do seu nome é {nome[-1]}')
else:
     print("Desculpe, você deixou campos vazios.")

