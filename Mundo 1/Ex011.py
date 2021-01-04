# EXERCICIO 011
# Exercício Python 11: Faça um programa que leia a
# largura e a altura de uma parede em metros, calcule
# a sua área e a quantidade de tinta necessária para
# pintá-la, sabendo que cada litro de tinta pinta uma
# área de 2 metros quadrados.

larg = float(input('Largura: '))
alt = float(input('Altura:'))
area = larg * alt
tinta = area / 2

print('A sua parede mede {:.2f}m x {:.2f}m e tem no total {:.2f}m2'.format(larg, alt, area))
print('Você vai precisar de {:.2f}l de tinta.'.format(tinta))
