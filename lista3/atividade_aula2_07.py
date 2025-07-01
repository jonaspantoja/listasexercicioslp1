'''
FATEC -   Programação de computadores
Exercício 7 - IMC
Jonas Fernando Pantoja
'''

#Declarando as variáveis e recebendo os dados do usuário

peso = float(input("Informe o seu peso em Kg:"))
altura = float(input("Informe a sua altura em metros:"))
resultado = peso/altura**2

'''Processando os dados e preparando a saída
IMC = PESO/(ALTURA²)
- MENOR QUE 17 = MUITO ABAIXO DO PESO
- ENTRE 17 E 18.49 = ABAIXO DO PESO
- ENTRE 18.5 E 24.99 = PESO NORMAL
- ENTRE 25 E 29.99 = ACIMA DO PESO
- ENTRE 30 E 34.99 = OBESIDADE I
- ENTRE 35 E 39.99 = OBESIDADE II
- IGUAL OU MAIOR QUE 40 = OBESIDADE III
'''

if(resultado < 17):
    print("Seu IMC é ",resultado, "você está MUITO ABAIXO DO PESO.")
elif(resultado >=17 and resultado <=18.49):
    print("Seu IMC é ",resultado, "você está ABAIXO DO PESO.")
elif(resultado >= 18.5 and resultado <=24.99):
    print("Seu IMC é ",resultado, "você está com o PESO NORMAL.")
elif(resultado >= 25 and resultado <=29.99):
    print("Seu IMC é ",resultado, "você está ACIMA DO PESO.")
elif(resultado >= 30 and resultado <=34.99):
    print("Seu IMC é ",resultado, "você está com OBESIDADE GRAU I.")
elif(resultado >= 35 and resultado <=39.99):
    print("Seu IMC é ",resultado, "você está com OBESIDADE GRAU II.")
else:
    print("Seu IMC é ",resultado, "você está com OBESIDADE GRAU III.")








