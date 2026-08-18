import os

def limpador_de_tela():
    os.system('cls')


def continuador():
    while True:
        esc = input('Deseja continuar? (S/N)').lower().strip()
        if esc in ['s', 'n']:
            break
        else:
            print('Digite apenas S ou N.')
    return esc
