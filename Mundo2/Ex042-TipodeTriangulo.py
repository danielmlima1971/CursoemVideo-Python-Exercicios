# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo
# será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

print('TIPOS DE TRIÂNGULOS')
s1 = float(input('Digite o tamanho do segmento 1: '))
s2 = float(input('Digite o tamanho do segmento 2: '))
s3 = float(input('Digite o tamanho do segmento 3: '))


if (s1 + s2 < s3) or (s1 + s3 < s2) or (s2 + s3 < s1):
    print('Não pode ser formado um triângulo com esses segmentos')
elif s1 == s2 and s2 == s3:
    print('O triângulo é EQUILÁTERO')
elif (s1 == s2 and s1 != s3) or (s1 == s3 and s1 != s2) or (s2 == s3 and s2 != s1):
    print('O triângulo é ISÓSCELES')
elif (s1 != s2 and s2 != s3 and s3 != s1):
    print('O triângulo é ESCALENO')



