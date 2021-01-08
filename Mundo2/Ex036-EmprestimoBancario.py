# Exercício Python 36: Escreva um programa para aprovar
# o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em
# quantos anos ele vai pagar. A prestação mensal não pode
# exceder 30% do salário ou então o empréstimo será negado.

print('\033[7;30;41m=\033[m' * 21)
print('\033[7;30;41m EMPRESTIMO BANCÁRIO \033[m')
print('\033[7;30;41m=\033[m' * 21)

casa = float(input('Qual o valor da casa? '))
prazo = int(input('Qual o prazo de pagamento? (em anos) '))
sal = float(input('Qual sua renda média mensal? '))

prazo = prazo * 12
parcela = casa / prazo

print('Valor da casa: R$ {:.2f}'.format(casa))
print('Valor da Parcela: R$ {:.2f}'.format(parcela))

if parcela > (sal * 0.30):
    print('Você NÃO será aprovado pois seu salário (R$ {:.2f}) é baixo '
          '\npara a parcela de R$ {:.2f}'.format(sal, parcela))
else:
    print('Você será aprovado pois pode pagar uma '
          '\nparcela de R$ {:.2f} com o salário de R$ {:.2f}'.format(parcela,
                                                                                                           sal))
