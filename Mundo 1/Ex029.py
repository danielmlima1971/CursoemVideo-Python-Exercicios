#
# Exercício Python 29: Escreva um programa que leia a
# velocidade de um carro. Se ele ultrapassar 80Km/h, mostre
# uma mensagem dizendo que ele foi multado. A multa vai
# custar R$7,00 por cada Km acima do limite.

vel = int(input('Qual a velocidade do veículo? '))

if vel <= 80:
    print('VOCÊ ESTÁ DENTRO DO LIMITE DE VELOCIDADE PERMITIDO PRA ESSA VIA!!')
else:
    print('MULTADO!!')
    multa = (vel - 80) * 7
    print('O valor da sua multa será de R$ {:.2f}'.format(multa))
print('TENHA UM BOM DIA, DIRIJA COM SEGURANÇA!')