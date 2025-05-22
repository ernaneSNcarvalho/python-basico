'''
    F-STRINGS
'''

nome = 'Biro Biro'
altura = 1.89
peso = 99
imc = peso / altura ** 2

texto = f'{nome} tem {altura:.2f} de altura e pesa {peso} quilos e seu imc e de {imc:.2f}'

print(texto)

# FORMAT

a = 'Alberto'
b = 'Bruno'
c = 'Camilo'
d = 2.20

string = 'a={} b={} c={} d={:.2f}' # Se colocar mais um sem referencia ele vai dar erro out of range
formato = string.format(a, b, c, d)

print(formato)

