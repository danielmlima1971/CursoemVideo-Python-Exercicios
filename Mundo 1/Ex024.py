# EXERCICIO 024
# Exercício Python 24: Crie um programa que leia o nome
# de uma cidade diga se ela começa ou não com o nome “SANTO”.

cid = str(input('Digite um nome de cidade: '))
cidade = cid.lower()

if (cidade.find("santo") > -1):
    print('A nome da cidade digitado é {}'.format(cidade.title()))
    print('A cidade tem a palavra "Santo" em seu nome')
else:
    print('A nome da cidade digitado é {}'.format(cidade.title()))
    print('A cidade não tem a palavra "Santo" em seu nome')

