'''
FATEC -   Programação de computadores
Exercício 2 - Classificação de notas
Jonas Fernando Pantoja
'''

# Declarando as variáveis

nota = int(input("Digite a nota (entre 0 e 100)"))


# Processando os dados

if nota >= 90:
    print("Aprovado com excelência")

elif nota >=70 and nota <89:
    print("Aprovado")

elif nota >=50 and nota < 69:
    print("Recuperação")

else:
    print("Reprovado")
