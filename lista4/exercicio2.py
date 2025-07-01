'''
FATEC RIO CLARO
INTELIGÊNCIA ARTIFICIAL
LINGUAGEM DE PROGRAMAÇÃO I
DOCENTE: ORLANDO SARAIVA JÚNIOR
DISCENTE: JONAS PANTOJA
'''
# EXIBIR TODOS OS MÚLTIPOS DE 5 ENTRE 5 E 50

from time import sleep
print("Exibindo todos os múltiplos de 5 no intervalo de 5 a 50 utilizando FOR:")

numero = 5 

for numero in range(5,51):
    if numero % 5 == 0:
        print(numero)
        sleep(1)
