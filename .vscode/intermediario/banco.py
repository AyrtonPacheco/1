print('Seja bem vindo ao Banco Carioca *RJ40* o seu banco nas alturas!')
nome = input('Por gentileza, qual é o seu nome? ')
emprestimo = input(f' Bem vindo Sr[a]{nome}, qual o valor do emprestimo que deseja hoje? ')
print('*INFORMAÇÃO IMPORTANTE*, receberá uma acréscimo de 20%. ')
parcelas = input('Em quantas parcelas deseja quitar sua dívida? ')

valor_emprestimo = int(emprestimo)
quantas_parcelas = int(parcelas)

valor_total = ((valor_emprestimo * 1.20) / quantas_parcelas)
juros = (valor_emprestimo * 0.20)

print(f'O valor que você irá pagar de juros será:R${juros}!')
print(f'Seu emprestimo de: R${emprestimo} terá {parcelas}x parcelas de R${valor_total}')
print('Obrigado por utilizar o nosso Banco Carioca, esperamos vé-lo em breve!')