# Exercício Python 39: Faça um programa que leia o
# ano de nascimento de um jovem e informe, de acordo
# com a sua idade, se ele ainda vai se alistar ao
# serviço militar, se é a hora exata de se alistar
# ou se já passou do tempo do alistamento. Seu programa
# também deverá mostrar o tempo que falta ou que passou
# do prazo.

import datetime
ano = int(input('Digite seu ano de nascimento: '))
data = datetime.date.today().year
if data - ano < 18:
    print('Você ainda vai precisar se alistar')
elif data - ano == 18:
    print('Este é o ano do seu alistamento')
else:
    dif = data - ano - 18
    print('Você era para ter se alistado {} anos atrás, se alistou?'.format(dif))


