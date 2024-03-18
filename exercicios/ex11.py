largura = float(input('Largura da sua parede: '))
altura = float(input('Altura da sua parede: '))
area = largura*altura
print(f'Sua parede tem a dimensão de; {largura} x {altura} e sua área é de: {area}m2.')
print('Considerando a cada 2m de parede, necessita de 1l de tinta.')
tinta = area / 2
print(f'Para a parede ser pintada, será necessário: {tinta}l de tinta.')