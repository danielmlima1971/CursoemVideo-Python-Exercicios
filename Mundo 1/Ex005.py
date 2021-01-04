# Ordem de precedência
# 1 - ()
# 2 - ** (potenciação)
# 3 - * / // %
# 4 - + -

# AULA 07A
''' (três aspas simples abrem e fecham um bloco de comentário)
nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:=^20}!'.format(nome))
#Entre chaves pode ser usado    {:20} para usar 20 espaços.
#                               {:>20} Para alinhar na direita.
#                               {:^20} Para centralizar.
#                               {:=^20} Para =======Daniel=======!

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
pot = n1 ** n2
mult = n1 * n2
div = n1 / n2
di = n1 // n2
mod = n1 % n2
s = n1+n2
sub = n1 - n2

print('A potenciação é {} \nA multiplicação é {} \nA divisão é {:.2} \nA divisão inteira é {}'.format(pot, mult,
                                                                                                         div, di))
print('O módulo é {} \nA soma é {} \nA subtração é {}'.format(mod,s,sub))
'''
# EXERCÍCIO 005
# MOSTRAR O SUCESSOR E O ANTECESSOR DE UM NÚMERO

n1 = int(input('Digite um número: '))
s = n1 + 1
a = n1 - 1
print('O número digitado foi: {} \nSeu sucessor é: {} \nSeu antecessor é: {}'.format(n1, s, a))
# Outra solução utilizando apenas uma variável:
# print('O número digitado foi: {} \nSeu sucessor é: {} \nSeu antecessor é: {}'.format(n1, (n+1), (n-1)))
