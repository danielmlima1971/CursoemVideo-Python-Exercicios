#
# Exercício Python 32: Faça um programa que leia
# um ano qualquer e mostre se ele é bissexto.

from datetime import date
import termcolor
ano = int(input('Digite o ano: '))

if ano <= 0:
    ano = date.today().year
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print(termcolor.colored('{} é um ano bissexto'.format(ano), 'green'))
else:
    print(termcolor.colored('{} não é um ano bissexto'.format(ano), 'red'))

