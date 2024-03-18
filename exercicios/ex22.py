name = str(input('Digite seu nome completo: ').strip())
print(f'Seu nome compelto é: {name}')

print(f'Seu nome todo em maísculo: {name.upper()}')

print(f'Seu nome todo em minusculo: {name.lower()}')


print(f'Seu nome tem {len(name) - name.count(' ')}, letras ao todo.')

nome1 = name.split()
print(f'O seu primeiro nome é: {nome1[0]}, ao todo tem: {len(nome1[0])}.')
