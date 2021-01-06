# Exercício Python 038: Escreva um programa que leia dois números
# inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print('O primeiro número ({}) é maior que o segundo número ({})'.format(n1, n2))
elif n2 > n1:
    print('O segundo número ({}) é maior que o primeiro número ({})'.format(n2, n1))
else:
    print('Os números são iguais!')