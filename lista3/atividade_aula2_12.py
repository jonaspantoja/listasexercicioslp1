'''
FATEC -   Programação de computadores
Exercício 12 -
Jonas Fernando Pantoja
'''

temp = float(input("Informe uma temperatura em graus celsius:"))

if temp <= 15:
    print('Frio')
elif (temp > 15 and temp <=25):
    print("Agradável")
else:
    print('Quente')
