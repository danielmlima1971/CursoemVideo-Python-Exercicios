# EXERCICIO 008
# Exercício Python 8: Escreva um programa que leia
# um valor em metros e o exiba convertido em centímetros
# e milímetros.

n1 = float(input('Qual o valor em metros? '))
print('{} metro(s) tem {} centímetros e {} '
      'milímetros!'.format(n1, (n1*100), (n1*1000)))
