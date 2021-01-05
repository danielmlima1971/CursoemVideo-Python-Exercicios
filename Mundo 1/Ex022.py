# EXERCICIO 022
# Exercício Python 22: Crie um programa que leia o nome
# completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: '))

print('Seu nome com todas as letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome com todas as letras minúsculas é {}'.format(nome.lower()))
print('Seu nome tem {} caracteres'.format(len(nome.replace(" ", ""))))
dividido = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(dividido[0])))
