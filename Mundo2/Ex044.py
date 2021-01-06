# Exercício Python 44: Elabore um programa que calcule o valor
# a ser pago por um produto, considerando o seu preço normal e
# condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço normal
# – 3x ou mais no cartão: 20% de juros.

print('CALCULAR PAGAMENTO')
valor = float(input('Valor do produto R$ '))
print('''Escolha a forma de pagamento:
[1] - Á vista com 10% de desconto
[2] - À vista no cartão com 5% de desconto
[3] - Até 2x no cartão sem desconto
[4] - 3x ou mais no cartão com 20% de acréscimo
''')

while(True):
    pgto = int(input('Escolha a forma de pagamento: '))

    if  pgto == 1:
        print('Você escolheu pagar à vista, '
              '\nseu produto custará R$ {:.2f} com 10% de desconto.'.format(valor * 0.90))
        break
    elif pgto == 2:
        print('Você escolheu pagar à vista no cartão, '
              '\nSeu produto custará R$ {:.2f} com 5% de desconto.'.format(valor * 0.95))
        break
    elif pgto == 3:
        print('Você escolheu pagar em até 2x no cartão,'
              '\nseu produto custará R$ {:.2f}'.format(valor))
        break
    elif pgto == 4:
        print('Você escolheu parcelar em 3x ou mais no cartão,'
              '\nseu produto custará R$ {:.2f} com acréscimo de 20%'.format(valor * 1.2))
        break
    else:
        print('\033[31mOpção INVÁLIDA, escolha uma das opções apresentadas\033[m')
# Adicionei um bloco while pois se o usuário digitar uma opção inválida
# o programa vai perguntar novamente após o aviso, se escolher uma
# opção válida, o programa dá um break dentro do bloco.