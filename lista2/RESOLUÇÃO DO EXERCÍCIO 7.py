'''
FATEC
INTELIGÊNCIA ARTIFICIAL
LABORATÓRIO DE PROGRAMAÇÃO
LISTA DE EXERCÍCIOS 2
RESOLUÇÃO DO EXERCÍCIO 7
JONAS FERNANDO PANTOJA
'''

# Declarando as variáveis e recebendo os dados

primeiro_nome = str(input("Qual é o seu primeiro nome?"))

ano_nascimento = str(input("EM qual ano você nasceu?"))

identificador = f"{primeiro_nome}{ano_nascimento}"
#Exibindo a mensagem

print(" Seu identificador de usuário é:",identificador,".")
