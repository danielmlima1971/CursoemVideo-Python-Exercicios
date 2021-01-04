# EXERCICIO 018
# Exercício Python 18: Faça um programa que leia um
# ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.

import math
n1 = float(input('Digite o angulo q deseja: '))
sen = math.sin(math.radians(n1))
cos = math.cos(math.radians(n1))
tan = math.tan(math.radians(n1))

print('O seno do numero digitado é {:.2f} \nO coseno do número é {:.2f} \nA tangente do número é {:.2f}'.format(sen, cos, tan))
