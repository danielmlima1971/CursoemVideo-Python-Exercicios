# EXRCICIO 010
# Exercício Python 10: Crie um programa que leia
# quanto dinheiro uma pessoa tem na carteira e
# mostre quantos dólares ela pode comprar.

real = float(input('Quantos reais você tem? R$ '))
dol = real / 3.27
print('Com R$ {:.2f} você pode comprar US$ {:.2f}.'.format(real, dol))

