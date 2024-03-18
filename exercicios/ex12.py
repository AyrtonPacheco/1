product = float(input('Qual é o valor do produto? '))
promo = product-(product*5 / 100)
print(f'O produto que custava R${product:.2f}, na promoção de 5% OFF vai custar R${promo:.2f}')