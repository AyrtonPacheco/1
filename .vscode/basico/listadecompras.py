"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
#lista = ['Maria', 'Helena', 'Luiz']
#lista.append('João')

#for indice, nome in enumerate(lista):
#    print(indice, nome, lista[indice])

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)


# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')
    

# Criar uma lista vazia para a lista de compras
lista_de_compras = []

# Função para adicionar itens à lista de compras
def adicionar_item():
    item = input("Digite o item que deseja adicionar à lista de compras: ")
    lista_de_compras.append(item)
    print(f"{item} foi adicionado à lista de compras.")

# Função para exibir a lista de compras
def exibir_lista():
    print("Lista de Compras:")
    for item in lista_de_compras:
        print(item)

# Loop principal
while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar item à lista")
    print("2. Exibir lista de compras")
    print("3. Sair")

    escolha = input("Digite o número da opção: ")

    if escolha == '1':
        adicionar_item()
    elif escolha == '2':
        exibir_lista()
    elif escolha == '3':
        print("Saindo da lista de compras. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")