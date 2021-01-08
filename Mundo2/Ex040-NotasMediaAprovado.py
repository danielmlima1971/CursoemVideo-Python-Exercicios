# Exercício Python 040: Crie um programa que leia duas notas
# de um aluno e calcule sua média, mostrando uma mensagem
# no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

print('NOTAS DO ALUNO')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2) / 2

print('A média do Aluno é {}, portanto o'.format(media))
if media < 5:
    print('aluno está REPROVADO')
elif media >= 5 and media < 7:
    print('aluno está em RECUPERAÇÃO')
elif media >= 7:
    print('aluno está APROVADO')
