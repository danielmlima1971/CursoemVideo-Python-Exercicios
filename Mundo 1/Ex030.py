# EXERCÍCIO 030
# Exercício Python 30: Crie um programa que leia um
# número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

import termcolor
num = int(input('Digite um número: '))

if num % 2 == 0:
    print(termcolor.colored('O número digitado é PAR', 'green'))
else:
    print(termcolor.colored('O número digitado é IMPAR', 'red'))
