
'''
    Interpolacao basica de strings
    s - string
    d e i - int
    f - float 
    x e X - Hexadecimal (ABCDEF0123456789)
'''

nome = 'Luiz'
preco = 1000.999388487
variavel = '%s, o preco e de R$%.2f' % (nome, preco)

print(variavel)
print('O hexadecimal de %d e %08X' %(1500, 1500))