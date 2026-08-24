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

def adicionar(msg, saldef, tipo, dicionario):
    if tipo <= len(dicionario) and tipo > 0:
        a = float(input(msg))
        if a > saldef:
            print('Erro. Valor > Salário')
        else:
            tipo = str(tipo)
            nums = {
                '1': 'Transporte',
                '2': 'Alimentação',
                '3': 'Lazer',
                '4': 'Conta de água',
                '5': 'Conta de luz',
                '6': 'Escola/Faculdade',
                '7': 'Internet'
            }
            dicionario[nums[tipo]] += a
            print('Adicionado com sucesso')
        return dicionario
    else:
        print('Erro.')


def tela_inicial():
    from datetime import date
    print('-' * 30)
    print(date.today())
    print('-' * 30)
    print('GERENCIADOR DE GASTOS SIMPLES')
    print('-' * 30)

def saidorsimples():
    from time import sleep as s
    print('Saindo...')
    s(1)

def porcentador(valor):
    if valor > 0:
        return f'{valor:.2f}%'
    else:
        return ''

def Rendador():
    try:
        with open('renda.txt', 'r') as renda:
            valor = renda.read()
            return float(valor)
    except (FileNotFoundError, ValueError):
        valor = LeiaDinheiro('Digite seu sálario')
        with open('renda.txt', 'w') as renda:
            renda.write(str(valor))
        return valor

def NovaRenda():
    a = LeiaDinheiro('Digite sua nova renda:\n')
    with open('renda.txt', 'w') as renda:
        renda.write(str(a))
        return a


def LeiaDinheiro(msg):
    while True:
        valor = input(msg)
        if ',' in valor:
            antesvi, depoisvi = valor.split(',')
            if antesvi.isnumeric() and depoisvi.isnumeric():
                valor = '.'.join([antesvi, depoisvi])
                valor = float(valor)
                return valor
        elif valor.isnumeric():
            valor = float(valor)
            return valor
        else:
            print(f'{valor} é inválido')
