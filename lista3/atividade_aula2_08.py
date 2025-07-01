'''
FATEC -   Programação de computadores
Exercício 8 - Triângulo
Jonas Fernando Pantoja
'''

# Recebendo os dados do usuário

lado1 = float(input(" Digite o tamanho do lado 1 em centímetros:"))
lado2 = float(input(" Digite o tamanho do lado 2 em centímetros:"))
lado3 = float(input(" Digite o tamanho do lado 3 em centímetros:"))

#Verificando se forma um triângulo


if (lado1 + lado2 > lado3 and lado3 + lado2 > lado1 and lado3 + lado1 > lado2):
    print("Esses lados podem formam um triângulo ",end="")
    if (lado1 == lado2 == lado3):
        print("equilátero.")
    elif (lado1 != lado2 != lado3 != lado1):
        print("escaleno.")
    else:
        print("isóceles.")
else:
    print("Esses comprimentos não podem formam um triângulo")

     
