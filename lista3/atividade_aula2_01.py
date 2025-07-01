

'''
FATEC - Programação de computadores
Exercício 1: Benefício
Jonas Fernando Pantoja
'''

# Declarando as variáveis

idade = int(input("Qual é a sua idade?"))


salario = float(input("Qual é o seu salário?"))

# Processando os dados e informando o resultado

if idade >= 60:
    print("Você tem direito ao benefício")

elif idade >=18 and salario <= 2000:
    print("Você tem direito ao benefício")

else:
    print("Você não tem direito ao benefício")

