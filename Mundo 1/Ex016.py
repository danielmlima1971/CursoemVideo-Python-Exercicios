# EXERCICIO 016
# Exercício Python 16: Crie um programa que leia um número
# Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc
n1 = float(input('Digite um numero com várias casas decimais: '))
trunc = trunc(n1)

print('O número que vc digitou {} sem os decimais é: {}'.format(n1, trunc))
print('O número que vc digitou {} sem os decimais é: {}'.format(n1, int(n1)))

# Podemos truncar o número usando também int(n1)