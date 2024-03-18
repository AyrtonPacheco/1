import math
co = float(input('Digite o valor do seu cateto oposto: '))
ca = float(input('Digite o valor do seu cateto adjacente: '))
hipo = math.hypot(ca, co)
print(f'Logo o valor da sua hipotenusa é de: {hipo:.2f}')