# EXERCICIO 026
# Exercício Python 26: Faça um programa que leia uma
# frase pelo teclado e mostre quantas vezes aparece a
# letra “A”, em que posição ela aparece a primeira vez
# e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip().lower()

print('A frase contém {} vezes a letra A'.format(frase.count('a')))
print('Ela aparece pela primeira vez na posição {}'.format(frase.find('a')+1))
print('Ela aparece pela última vez na posição {}'.format(frase.rfind('a')+1))
