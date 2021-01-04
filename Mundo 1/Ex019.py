# EXERCICIO 019
# Exercício Python 19: Um professor quer sortear um dos seus
# quatro alunos para apagar o quadro. Faça um programa que
# ajude ele, lendo o nome dos alunos e escrevendo na tela o
# nome do escolhido.

import random

a1 = input('Nome do Aluno 01: ')
a2 = input('Nome do aluno 02: ')
a3 = input('Nome do aluno 03: ')
a4 = input('Nome do aluno 04: ')
lista = [a1, a2, a3, a4]
sortudo = random.choice(lista)
print('O aluno sorteado é {}'.format(sortudo))
