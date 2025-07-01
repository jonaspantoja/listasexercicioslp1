'''
FATEC -   Programação de computadores
Exercício 10 -
Jonas Fernando Pantoja
'''

ano = int(input("Digite o ano com quatro dígitos:"))

if ((ano % 4 == 0 and ano % 100 != 0) or (ano % 4 == 0 and ano % 100 != 0 and ano % 400 == 0)):
    print("Ano bissexto")
else:
    print("Não é um ano bissexto")
