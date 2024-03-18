lista = []
nao_opcao = 'i a l'

while True:
    print('Bem vindo ao seu APP de compras')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao not in nao_opcao:
        print('Por favor, digite (i), (a) ou (l)')
        continue

    if opcao == 'i':
        valor = input('Valor: ')
        print(f'{valor}, foi adicionado a sua lista.')
        lista.append (valor)

    elif opcao == 'a':
        indice_str = input('Selecione o indice que deseja apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]

        except IndexError:
            print('Por favor, siga as instruções.')
        except ValueError:
            print('Por favor, siga as instruções.')
        except SyntaxError:
            print('Por favor, siga as instruções.')

    elif opcao == 'l':
        
        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)



    

