#Ordem de Precedência:
#1 ()
#2 **
#3 * / // %
#4 + - 

n = int(input('Digite um valor: '))

print(f'Analisando o número {n}, o seu antecessor é:{n - 1} | e o seu sucessor é:{n + 1}')

print('='*100)

n1 = int(input('Digite um novo valor: '))
print(f'O número digitado foi: {n1}.\n O seu dobro é: {n1 * 2}.\n O seu triplo é: {n1 * 3}.\n Sua raiz quadrada é {n1**2}. ')

print('='*100)

print('Bem vindo ao Portal do Colégio Cena')
nome = input('Digite seu nome: ')
nota1 = 6
nota2 = 6
media = (nota1 + nota2) / 2
print(f'Sua nota em matemática foi: {nota1}.')
print(f'Sua nota em português foi: {nota2}.')
print(f'A média atual é: {media:.0f} ')

