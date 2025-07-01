'''
FATEC
INTELIGÊNCIA ARTIFICIAL
LABORATÓRIO DE PROGRAMAÇÃO
LISTA DE EXERCÍCIOS 2
RESOLUÇÃO DO EXERCÍCIO 8
JONAS FERNANDO PANTOJA
'''

# Declarando as variáveis e recebendo os dados

preco_original = float(input("Qual é o preço em reais sem desconto?"))

desconto = float(input("Qual é o desconto em porcentagem (0 a 100)?"))

# Exibindo a mensagem

print("O produto que custava R$: ", preco_original, " com o desconto de ", desconto, "%, agora custa R$: ", preco_original - (preco_original*(desconto/100)),".") 
