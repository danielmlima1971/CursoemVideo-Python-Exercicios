# EXERCICIO 35
# Exercício Python 35: Desenvolva um programa que leia o comprimento
# de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-=-' *9)
print('ANALISADOR DE TRIANGULOS')
print('-=-' *9)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Estes segmentos podem formar um trângulo')
else:
    print('Estes segmentos NÃO podem formar um triângulo')
