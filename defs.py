

def limpador_de_tela():
    import os
    os.system('cls')


def continuador():
    while True:
        esc = input('Deseja continuar? (S/N)').lower().strip()
        if esc in ['s', 'n']:
            break
        else:
            print('Digite apenas S ou N.')
    return esc

def adicionar(msg, var, saldef):
    a = float(input(msg))
    if a > saldef:
        print('Erro. Valor > Salário')
    else:
        var += a
        print('Adicionado com sucesso')
    return var


def tela_inicial():
    from datetime import date
    print('-' * 30)
    print(date.today())
    print('-' * 30)
    print('GERENCIADOR DE GASTOS SIMPLES')
    print('-' * 30)


