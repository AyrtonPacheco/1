"""
PARA ADCIONAR CORES NO SEU TERMINAL VAMOS ENTENDER QUE FUNCIONA DESSA FORMA:
\033[O;33;44m]
**SEMPRE COMEÇA COM BARRA INVERTIDADE (\) E O NUMERO 033;**
\033

PRIMEIRO NUMERO VAI SER O STYLE DA FONTE, SEJA EM NEGRITO, SUBLINHADO ENTRE OUTROS NESTE CASO (0;)
SEGUNDO NUMERO VAI SER O TEXT DO SEU CODIGO, NESTE CASO (0;33;)
TERCEIRO NUMERO VAI SER O BACK DO SEU CODIGO, NESTE CASO (0;33;44)
E SEMPRE TERMINA COM A LETRA m NO FINAL DO SEU CODIGO, NESTE CASO (0;33;44m)

"""
a = 3
b = 5
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}.')