# EXERCICIO 015
# Exercício Python 15: Escreva um programa que pergunte a
# quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule
# o preço a pagar, sabendo que o carro custa R$60 por dia
# e R$0,15 por Km rodado.

km = int(input('Quantos Km foram percorridos? '))
dias = int(input('Quantas diárias foram utilizadas? '))
pagar = (km * 0.15) + (dias * 60)

print('O veículo foi utilizado por {} dias e percorreu {}Km'.format(dias, km))
print('O total a pagar é R$ {:.2f}'.format(pagar))