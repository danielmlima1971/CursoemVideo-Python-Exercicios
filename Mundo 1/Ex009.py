# EXERCICIO 009
# Exercício Python 9: Faça um programa que leia um
# número Inteiro qualquer e mostre na tela a sua tabuada.

n1 = int(input('Digite um número: '))
x=1
for x in range (1, 11):
    print('{} x {:>2} = {:>3}'.format(n1,x,(n1*x)))

# A solução do exercício diz pra fazer 10 linhas de print
# mas eu usei um "for" pra melhorar o processo.