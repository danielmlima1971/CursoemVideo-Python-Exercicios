# EXERCICIO 34
# Exercício Python 34: Escreva um programa que pergunte o salário
# de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1250,00, calcule um aumento de 10%. Para os
# inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o salário: '))

if salario <= 1250:
    sal = salario * 1.15
else:
    sal = salario * 1.10
print('O salário de R$ {:.2f} passará a ser R$ {:.2f}'.format(salario, sal))