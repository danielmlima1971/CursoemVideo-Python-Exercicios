# EXERCICIO 014
# Exercício Python 14: Escreva um programa que converta
# uma temperatura digitando em graus Celsius e converta
# para graus Fahrenheit.

celsius = float(input('Quantos graus celsius você quer converter? '))
fahren = celsius * 1.8 + 32
print('{:.1f}ºC correspondem a {:.1f}ºF'.format(celsius, fahren))
fahren = float(input('Quantos graus fahrenheit você quer converter? '))
celsius = (fahren - 32) / 1.8
print('{:.1f}ºF correspondem a {:.1f}ºC'.format(fahren, celsius))