# Exercício Python 45: Crie um programa que faça o
# computador jogar Jokenpô com você.

import random

c = 0 # Placar do computador
u = 0 # Placar do usuário
print('JOKEMPÔ GAME')

while True:
    print('''escolha sua opção:
[1] Pedra [2] Papel [3] Tesoura [4] SAIR DO JOGO''')
    comp = random.choice(['Pedra', 'Papel', 'Tesoura'])
    #print('O computador escolheu {}'.format(comp))
    print('O jogo está computador {} x {} você.'.format(c, u))

    while True:
        try:
            usuario = int(input('Digite sua opção: '))
        except ValueError:
            print('\033[1;31mVocê digitou uma opção INVÁLIDA!\033[m')
            print('''escolha sua opção:
            [1] Pedra [2] Papel [3] Tesoura [4] SAIR DO JOGO''')
            comp = random.choice(['Pedra', 'Papel', 'Tesoura'])
            print('O jogo está computador {} x {} você.'.format(c, u))

            continue
        else:
            break

    if usuario == 1:
        usuario = 'Pedra'
    elif usuario == 2:
        usuario = 'Papel'
    elif usuario == 3:
        usuario = 'Tesoura'
    elif usuario == 4 :
        print('\033[1;31mJogo Encerrado\033[m')
        break
    else:
        print('\033[1;31mVocê digitou uma opção INVÁLIDA!\033[m')


    if usuario == 'Pedra' or usuario == 'Papel' or usuario == 'Tesoura':
        if (comp == 'Pedra' and usuario == 'Tesoura') or (comp == 'Papel' and usuario == 'Pedra') or (comp ==
                                                                                                      'Tesoura' and usuario == 'Papel'):
            print('O computador escolheu {} e você {}.'.format(comp, usuario))
            print('\033[1;31mPERDEU PLAYBOY!!\033[m')
            c += 1
        elif comp == usuario:
            print('O computador escolheu {} e você {}.'.format(comp, usuario))
            print('\033[1;32mEMPATARAM!!!\033[m')
        else:
            print('O computador escolheu {} e você {}.'.format(comp, usuario))
            print('\033[1;32mVocê GANHOU! PARABÉNS!!\033[m')
            u += 1

    # Jogo com opção de SAIR e reinicia automático, além de algumas validações.
    # Para ver se está funcionando bem habilite a linha 15.
