from time import sleep
salario = float(input('Qual é o seu salário atual?|R$ '))

aumento_10 = (salario*1.10) - salario
aumento_15 = (salario*1.15) - salario

if salario >= 1250:
    print(f"""               \033[32mPARABÉNS\033[m, 
Você teve um aumento salarial de 10% total de: \033[32mR${aumento_10:.2f}\033[m""")

    print(f'Logo seu salário atual é de: R${salario + aumento_10:.2f}')
else:
    print(f'PARABÉNS, você teve um aumento salarial de 15%total de: R${aumento_15:.2f}')

    print(f'Logo seu salário atual é de: R${salario + aumento_15:.2f}')
    

