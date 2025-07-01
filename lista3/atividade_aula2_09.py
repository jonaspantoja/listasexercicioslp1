'''
FATEC -   Programação de computadores
Exercício 9 -
Jonas Fernando Pantoja
'''

salario = float(input("Qual é o seu salário?"))

if salario<2000:
    print("Seu bônus é de 20%, ou seja, R$:", salario*0.2, ".")
elif  salario >= 2000 and salario <= 5000:
    print("Seu bônus é de 10%, ou seja, R$:", salario*0.1,".")
else:
    print("Seu bônus é de 5%, ou seja, R$: ",salario*0.05, ".")
    

