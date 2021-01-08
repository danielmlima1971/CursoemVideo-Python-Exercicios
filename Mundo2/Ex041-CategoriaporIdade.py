# Exercício Python 041: A Confederação Nacional de Natação
# precisa de um programa que leia o ano de nascimento de um
# atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
import datetime
print('CATEGORIA DO ATLETA')

nasc = int(input('Qual o ano de nascimento? '))
anoatual = datetime.date.today().year
idade = anoatual - nasc
print('O atleta tem {} anos de idade, portanto'.format(idade))

if idade <=9:
    print('está na categoria MIRIM')
elif idade <= 14:
    print('está na catogoria INFANTIL')
elif idade <= 19:
    print('está na catogoria JÚNIOR')
elif idade <= 25:
    print('está na catogoria SÊNIOR')
elif idade > 25:
    print('está na catogoria MASTER')
