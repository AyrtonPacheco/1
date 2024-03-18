"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
entrada = input('Digite um número: ')

if entrada.isdigit(): #Useu .isdigit porque a entrada não é uma string e sim um digito (numero)
    entrada_int = int(entrada) #transformei a entrada em int (numero)
    par_impar = entrada_int % 2 == 0 
    par_impar_texto = 'ímpar'
    
    if par_impar:
        par_impar_texto = 'par'
    print(f'Seu número {entrada_int} é {par_impar_texto}.')

else:
    print('Você não digitou um número. ')

