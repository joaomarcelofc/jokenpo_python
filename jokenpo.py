from random import randint
from time import sleep
contv = conte = contd = 0
while True:
    itens = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(0, 2)
    print('{:=^30}'.format(' JO KEN PO! '))
    print('''Suas opções
        [ 0 ] PEDRA
        [ 1 ] PAPEL
        [ 2 ] TESOURA ''')
    jogador = int(input('Qual é a sua jogada? '))
    print('JO...')
    sleep(0.5)
    print('KEN...')
    sleep(0.5)
    print('PO!!!')
    print('-='*15)
    print('Jogador jogou {}'.format(itens[jogador]))
    print('Computador jogou {}'.format(itens[computador]))
    print('-='*15)
    if computador == 0:
        if jogador == 0:
            print('EMPATE.')
            conte += 1
        elif jogador == 1:
            print('JOGADOR VENCEU!')
            contv += 1
        elif jogador == 2:
            print('COMPUTADOR VENCEU!')
            contd += 1
        else:
            print('JOGADA INVÁLIDA. Tente novamente.')
    elif computador == 1:
        if jogador == 0:
            print('COMPUTADOR VENCEU!')
            contd += 1
        elif jogador == 1:
            print('EMPATE.')
            conte += 1
        elif jogador == 2:
            print('JOGADOR VENCEU!')
            contv += 1
        else:
            print('JOGADA INVÁLIDA. Tente novamente')
    elif computador == 2:
        if jogador == 0:
            print('JOGADOR VENCEU!')
            contv += 1
        elif jogador == 1:
            print('COMPUTADOR VENCEU!')
            contd += 1
        elif jogador == 2:
            print('EMPATE.')
            conte += 1
        else:
            print('JOGADA INVÁLIDA. Tente novamente.')
    resposta = str(input('Deseja jogar novamente? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
print(f'Você ganhou {contv}, empatou {conte} e perdeu {contd} vezes.')
input('Pressione qualquer tecla para encerrar...')

