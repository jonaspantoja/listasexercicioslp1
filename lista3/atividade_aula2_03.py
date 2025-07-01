'''
FATEC -   Programação de computadores
Exercício 3 - IMC
Jonas Fernando Pantoja
'''

# Declarando as variáveis

altura = float(input("Digite a sua altura em metros"))

peso = float(input("Digite o seu peso em Kg"))

imc = peso/altura

# Processando os dados

if imc < 18.5:
    print("Abaixo do peso")

elif imc >=18.5 and imc <24.9:
    print("Peso normal")

elif imc >=25 and imc < 29.9:
    print("Sobrepeso")

elif imc >= 30 and imc < 34.9:
    print("Obesidade Grau 1")

elif imc >= 35 and imc < 39.9:
    print("Obesidade Grau 2")

else:
    print("Obesidade Grau 3 (mórbida)")
