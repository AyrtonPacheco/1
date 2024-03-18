
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é: ' ,nome)
    print(f'Sua idade é: ', idade)
    print(f'Seu nome invertido é: ',nome[::-1])
    print(f'A primeira letra do seu nome é: ',nome[0])
    print(f'A ultima letra do seu nome é: ',nome[-1::])
    print('Seu nome contém' ,(len(nome)), 'caracteres.')
    
#in foi usado para verificar se tinha espaços ' ' no nome da input.
    if ' ' in nome:
        print('Seu nome contém espaços.')
    else:
        print('Seu nome NÃO contém espaços.')
        

else:
    print('Desculpe, você deixou campos vazios.')





