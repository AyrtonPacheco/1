from random import randint

print('Seja bem vindo a Roleta da SORTE, Portugal de prêmios!')
print('Siga as instruções abaixo: ')
apostar = int(input('Digite um valor entre 1 a 12: '))

if apostar < 1 and apostar > 13:
    print('Por favor, digite apenas um número entre 2 a 12.')
else:
    print('Vez dos dados serem lançados.')
    dado1 = randint(1, 6)
    print(f'O valor do primeiro dado é: {dado1}')
    dado2 = randint(1, 6)
    print(f'O valor do primeiro dado é: {dado2}')
    
    soma = dado1 + dado2
    if soma == apostar:
        print('PARABÈNS, você ganhou na Roleta da SORTE! ')
        print(f'A soma deu: {soma}, e você apostou: {apostar}')

    else:
        print(f'VOCÊ PERDEU, sua aposta foi de: {apostar} tente novamente')

