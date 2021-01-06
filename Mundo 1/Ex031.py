#
# Exercício Python 31: Desenvolva um programa que pergunte
# a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45
# para viagens mais longas.

dist = int(input('Qual a distância da viagem? '))

if dist <= 200:
    valor = dist * 0.50
    print('O valor da passagem para percorrer {}Km é R$ {:.2f}'.format(dist, valor))
else:
    valor = dist * 0.45
    print('O valor da passagem para percorrer {}Km é R$ {:.2f}'.format(dist, valor))