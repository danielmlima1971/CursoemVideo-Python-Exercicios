# Exercício Python 51: Desenvolva um programa que leia o
# primeiro termo e a razão de uma PA. No final, mostre os
# 10 primeiros termos dessa progressão.

termo = int(input('Digite o termo da P.A.: '))
razao = int(input('Digite a razão da P.A.: '))
for c in range(1, 11):
    print('{}'.format(termo), end=' ')
    termo += razao
print('FIM')