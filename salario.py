nome = str(input('Informe o seu nome: '))
ganhos = float(input('Quanto você ganha por hora? R$'))
hr = float(input('Quantas horas você trabalha por dia? '))
dias = float(input('Quantas dias você trabalha por mês? '))

bruto = (ganhos * hr)*dias
ir = (bruto * 1.11)-bruto
inss = (bruto * 1.08)-bruto
sind = (bruto * 1.05)-bruto
descontos = ir + inss + sind
liquido = bruto - descontos
print(f'O seu salário bruto é de: R${bruto:.2f}')
print(f'Você declarou o IR desse ano e o valor foi de 11%, total de: R${ir:.2f}')
print(f'Você declarou o INSS desse ano e o valor foi de 8%, total de: R${inss:.2f}')
print(f'Você declarou o Sindicato desse ano e o valor foi de 5%, total de: R${sind:.2f}')
print(f'Com todos os descontos o salário liquido recebido é de R${liquido:.2f}')