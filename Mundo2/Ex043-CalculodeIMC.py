# Exercício Python 43: Desenvolva uma lógica que leia o peso e a
# altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida
# IMC = peso / altura ** 2

print('CALCULADORA DE IMC')
peso = float(input('Qual seu peso em Kg? '))
altura = float(input('Qual sua altura em metros? '))

imc = peso / altura ** 2
print('Seu IMC é {:.2f} portanto'.format(imc))

if imc < 18.5:
    print('você está abaixo do peso ideal. Engorde!')
elif imc < 25:
    print('você está no peso ideal, PARABÉNS!!')
elif imc < 30:
    print('você está com sobrepeso, cuidado, emagreça um pouco.')
elif imc < 40:
    print('você está OBESO, trate de emagrecer.')
else:
    print('sua obesidade é MÓRBIDA, procure um médico com URGÊNCIA!!')



