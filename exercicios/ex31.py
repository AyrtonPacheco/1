from time import sleep

dist = float(input('Qual é a distância da sua viagem? '))
km1 = 0.50 * dist
km2 = 0.45 * dist

if dist <= 200:
    print(f'Você está prestes a começar uma viagem de {dist:.2f}Km.')
    sleep(2)
    print(f'O preço da sua passagem será de: R${km1:.2f} reais.')

else:
    print(f'O preço da sua passagem será de: R${km2:.2f} reais')
