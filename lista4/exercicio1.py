'''
FATEC RIO CLARO
INTELIGÊNCIA ARTIFICIAL
LINGUAGEM DE PROGRAMAÇÃO I
DOCENTE: ORLANDO SARAIVA JÚNIOR
DISCENTE: JONAS PANTOJA
'''
# CONTAGEM DE 1 A 10 USANDO FOR E WHILE
# VOU ADICIONAR A BIBLIOTECA TIME PARA A CONTAGEM NÃO FICAR MUITO RÁPIDA

# USANDO A ESTRUTURA DE ITERAÇÃO WHILE

from time import sleep  #Importando apenas método de espera da biblioteca time

numero = 1

print('Contagem de 1 até 10 utilizando WHILE:')

while numero <= 10:
    print(numero)
    sleep(1)
    numero += 1
print ('Contagem com WHILE finalizada')

# USANDO A ESTRUTURA DE ITERAÇÃO FOR COMBINADA COM A FUNÇÃO RANGE

print('Contagem de 1 até 10 utilizando FOR:')
numero2 = 1

for numero2 in range (1,11):
    print(numero2)
    sleep(1)
print('Contagem com FOR finalizada')
    










