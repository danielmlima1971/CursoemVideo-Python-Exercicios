# Exercício Python 37: Escreva um programa em Python que
# leia um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão: 1 para binário,
# 2 para octal e 3 para hexadecimal.

n = int(input('Digite um número: '))

print('[1] Binário')
print('[2] Octal')
print('[3] Hexadecimal')
conv = int(input('Digite a opção desejada: '))

if conv == 1:
    res = bin(n)[2:]
    print('O número {} convertido para binário é {}'.format(n, res))
elif conv == 2:
    res = oct(n)[2:]
    print('O número {} convertido para Octal é {}'.format(n, res))
elif conv == 3:
    res = hex(n)[2:]
    print('O número {} convertido para Hexamedial é {}'.format(n, res))
else:
    print('Opção inválida, tente novamente!')
