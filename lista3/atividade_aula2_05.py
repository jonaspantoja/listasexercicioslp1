'''
FATEC -   Programação de computadores
Exercício 5 
Jonas Fernando Pantoja
'''

#Declarando as variáveis e recebendo os dados do usuário

num1 = float(input("Digite o número 1:"))
num2 = float(input("Digite o número 2:"))

#Processando os dados

if (num1 > num2):
    print("O número", num1, "é maior que o número", num2, ".")
elif (num1< num2):
    print("O número",num2, "é maior que o número",num1,".")
else:
    print("O número",num1," é igual ao número ",num2,".")
