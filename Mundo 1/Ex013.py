# EXERCICIO 013
# Exercício Python 13: Faça um algoritmo que leia o salário
# de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual o salário atual? R$ '))
aumento = float(input('Percentual de aumento a ser aplicado: '))
novo = salario + (salario * aumento /100)
print('O salário atual é R$ {:.2f} e o novo salário será R$ {:.2f}'.format(salario, novo))