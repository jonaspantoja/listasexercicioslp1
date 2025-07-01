'''
FATEC -   Programação de computadores
Exercício 6 
Jonas Fernando Pantoja
'''

#Declarando as variáveis e recebendo os dados do usuário

nota = float(input("DIgite a sua nota:"))

# processando os dados

if (nota >= 7):
    print("Aprovado")
elif(nota >=5 and nota<=6.9):
    print("Recuperação")
else:
    print("Reprovado")

