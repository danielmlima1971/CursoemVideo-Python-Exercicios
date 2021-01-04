# EXERCICIO 020
# Exercício Python 20: O mesmo professor do desafio 19 quer
# sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e
# mostre a ordem sorteada.

import random

a1 = input('Nome do Aluno 01: ')
a2 = input('Nome do aluno 02: ')
a3 = input('Nome do aluno 03: ')
a4 = input('Nome do aluno 04: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação vai ser {}'.format(lista))