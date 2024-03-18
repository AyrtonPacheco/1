"""
def welcome(nome, quantidade):#parametros
    print(f'Olá {nome} seja bem vindo.')
    print(f'Temos {quantidade}, em estoque.')

welcome('Ayrton', 2)#argumentos
"""
nome1 = input('Qual é o seu nome?  ')

def welcome(nome=nome1):
    print(f'Olá {nome} seja bem vindo.')

welcome(nome1)
welcome()


