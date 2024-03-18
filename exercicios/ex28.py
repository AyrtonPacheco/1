import random
from time import sleep

numero = random.randrange(0,5)

print('-'*100)
print('                   Bem vindo ao meu MUNDO, pensando em um número, tente advinha-lho!')
print('-'*100)

print('Vou pensar em um número de 0 a 5!')

n = int(input('Tente advinhar, qual número eu pensei? '))

print('PENSANDO...')
sleep(3)

if numero == n:
    print(f'O número escolhido foi: {n}')
    print('PARABÉNS! VOCÊ ME DERROTOU ')
else:
    print('HAHAHA, TENTE NOVAMENTE!')