# EXERCICIO 028
# Exercício Python 28: Escreva um programa que faça
# o computador “pensar” em um número inteiro entre
# 0 e 5 e peça para o usuário tentar descobrir qual
# foi o número escolhido pelo computador. O programa
# deverá escrever na tela se o usuário venceu ou perdeu.
import random
import time
sorteado = int(random.randint(1, 10))
# print('Pensei no número {}'.format(sorteado))
print('-=-' * 17)
print('Vou pensar em um número de 1 a 10, tente adivinhar-')
print('-=-' * 17)
num = int(input('Digite um número: '))
print('COMPUTANDO...')
time.sleep(4)

if num == sorteado:
    print('Parabéns!! Você acertou!! O número que eu havia pensado era exatamente {}'.format(sorteado))
else:
    print('Tente de novo, você errou! O número que eu pensei era {}'.format(sorteado))
print('Fim de Jogo')

