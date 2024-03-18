"""
import math 
print('-----Descobridor de raízes-----')
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'Você digitou {num}, e a sua raíz quadrada é: {raiz:.2f}')


PARA VOCE SABER USAR UM DETERMINADA FUNCIONALIDADE DE UMA BIBLIOTECA, VEJAMOS:
PRIMEIRO IMPORTEI MATH (import math)
JOGA EM UMA VARIÁVEL O QUE DESEJA SABER, EX:
raiz = math.sqrt(num)
QUERO SABER A RAIZ DE UM NUMERO, NO CASO (sqrt) seria a função e você põe em () sua variável, EX:
raiz = math.sqrt(num)
                MINHA VARIAVEL É (num), e quero saber a raiz dela.
OUTRO JEITO DE USAR SERIA.


from math import sqrt
print('-----Descobridor de raízes-----')
num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'Você digitou {num}, e a sua raíz quadrada é: {raiz:.2f}')
"""
import random
num = int(input('Digite um número e tente advinhar: '))
aleatorio = random.randrange(0, 5)

if num == aleatorio:
    print('Parabéns, você acertou!')
    
else:
    print(f'Tente novamente, o número correto era: {aleatorio}.')
    
