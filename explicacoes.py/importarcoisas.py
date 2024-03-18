"""
Para importar bibliotecas no python precisamos fazer desta forma:
EX:

import *bebidas* 
*NESTE CASO VOCE IMPORTARA TODAS AS BEBIDAS QUE ESTIVEREM EM (*bebidas*), como refri, agua, entre outros.

Usando um outro método mais especifico,
que no caso significa você importar algo especifico dentro de uma biblioteca.
EX:

from *bebida* import agua:
*NESTE CASO EU ESTOU IMPORTANDO UMA BIBLIOTECA DE (*bebida*) porém apenas o método/funcao (AGUA).
"""

import bebida #(GENERALIZA TUDO QUE ESTIVER EM BEBIDA)

#Duas coisas "IGUAIS", porém diferentes.

from bebida import agua #(ESPECIFICA APENAS O QUE QUER; NO CASO agua DA BIBLIOTECA bebida)
from bebida import agua,cafe #(ESPECIFICA APENAS O QUE QUER, NO CASO agua e cafe DA BIBLIOTECA bebida.)
"""
Você pode importar mais de uma coisa, apenas utilize ',' para separar.
EX:
from bebida import agua,cafe
"""