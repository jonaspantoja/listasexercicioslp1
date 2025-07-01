'''
FATEC -   Programação de computadores
Exercício 4 - IMC
Jonas Fernando Pantoja
'''

# Declarando variáveis

idade = int(input("Qual é a sua idade?"))

#Processando os dados

if (idade <12 or idade> 60):
    print("O Ingresso custa R$:15,00")
else:
    print("O Ingresso custa R$:30,00")
