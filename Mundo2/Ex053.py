# Exercício Python 53: Crie um programa que leia uma frase
# qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
# inverso == junto[::-1] PODE SER USADO EM VEZ DO FOR
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Temos um PALÍNDROMO')
else:
    print('NÃO É PALÍNDROMO')

