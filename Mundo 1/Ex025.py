#EXERCICIO 025
#Exercício  Python 25: Crie um programa que leia o nome de uma
# pessoa e diga se ela tem “SILVA” no nome.

n = str(input('Digite seu nome completo: '))
nome = n.lower()

if ('silva' in nome):
    print('Seu nome contém a palavra "Silva"')
else:
    print('Seu nome não tem a palavra "Silva"')