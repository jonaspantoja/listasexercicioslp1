'''
FATEC -   Programação de computadores
Exercício 11 -
Jonas Fernando Pantoja
'''

import random

num_aleatorio = random.randint(1,100)


print("O programa geou um número aleatório entre 1 e 100")

num_usuario = float(input('Qual número você acha que o programa gerou?'))
if (num_usuario > num_aleatorio):
    print('Muito alto.')
elif(num_usuario == num_aleatorio):
    print('Parabéns, o número gerado pelo programa foi',num_aleatorio, ' e você escolheu',num_usuario, '.')
else:
    print('Muito baixo')


print(f'O número gerado pelo sistema foi {num_aleatorio}, o número que vocÊ escolheu foi {num_usuario}')

                        
