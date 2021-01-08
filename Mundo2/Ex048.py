from time import sleep
soma = 0
for c in range(0,501,3):
    soma += c
    print(c)
    sleep(0.1)
print('A soma total é {}: '.format(soma))