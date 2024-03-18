"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
#print(variavel)
#print('O hexadecimal de %d é %08X' % (1500, 1500))

nome1 = 'Ze'
frase = '%s, é o nome do meu amigo' % (nome1)


nome2 = 'Fernanda'
frase1 = 'Eu amo minha mulher, %s' % (nome2)
print(frase1[::-1])
#Eu uso [::-1] para inverter toda a string ou frase seja o que estiver escrito sera invertido.
