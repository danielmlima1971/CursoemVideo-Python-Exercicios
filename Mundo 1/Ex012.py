# EXERCICIO 012
# Exercício Python 12: Faça um algoritmo que leia o preço
# de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Qual o preço do produto? '))
precoComDesconto = preco - (preco * 0.05)

print('O preço normal do produto é R$ {:.2f} e com 5% de desconto é R$ {:.2f}'.format(preco, precoComDesconto))
