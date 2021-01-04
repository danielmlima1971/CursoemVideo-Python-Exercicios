# EXERCICIO 017
# Exercício Python 17: Faça um programa que leia o
# comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo. Calcule e mostre o
# comprimento da hipotenusa.

import math

ca = float(input('Digite o 1o cateto: '))
co = float(input('Digite o 2o cateto: '))
print('A hipotenusa de {} e {} é {:.2f}'.format(ca, co, math.hypot(ca, co)))
