nome1 = input('Digite seu nome: ')
nome2= input('Digite outro nome: ')
contador = {}

def nome(input):#PARAMETRO E O QUE VOCE USA NA DEFINICAO (VARIAVEL)
    print(f'Olá, {nome1}! ') 
    print(f'Olá, {nome2}! ')

nome(0)#ARGUMENTO E O QUE VOCE PREENCHE DENTRO DA DEFINICAO

for letra in nome1:
    if letra.isalpha():
        contador[letra] = contador.get(letra, 0) + 1
        
print(f'Contagem de letras de:',nome1)
for letra, contagem in contador.items():
    print(f"{letra}: {contagem} vezes")


for letra in nome2:
    if letra.isalpha():
        contador[letra] = contador.get(letra, 0) + 1
        
print("Contagem de letras:",nome2)
for letra, contagem in contador.items():
    print(f"{letra}: {contagem} vezes")




    
    





