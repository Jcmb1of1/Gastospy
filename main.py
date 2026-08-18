import matplotlib.pyplot as plt
from datetime import date
from time import sleep as s
from defs import limpador_de_tela

#todas as variáveis constantes do projeto:

sal = float(input('Salário:\n'))
limpador_de_tela()

ali = tp = lz = gt = 0

g = {
    'Transporte': tp,
    'Aliimentação': ali,
    'Lazer': lz,
    'Gastos totais': gt
}

while True:
    limpador_de_tela()
    print(date.today())
    #tela inicial
    print('GERENCIADOR DE GASTOS SIMPLES')


    #escolha do usuário - o que ele quer fazer
    user = int(input('[1]Adicionar gastos\n[2]Ver gastos\n[3]Sair do sistema'))


    #escolha do usuário - que gasto ele quer adicionar
    if user == 1:
        limpador_de_tela()
        print('Qual tipo de gasto?')
        tipo = int(input('[1]Transporte\n[2]Alimentação\n[3]Lazer\n[4]Gastos Fixos'))
        if tipo == 1:
            limpador_de_tela()
            qtgast = float(input('Insira a quantidade gasta:\n'))
            tp += qtgast
            gt += qtgast
        elif tipo == 2:
            limpador_de_tela()
            qtgast = float(input('Insira a quantidade gasta:\n'))
            gt += qtgast
            ali += qtgast
        elif tipo == 3:
            limpador_de_tela()
            qtgast = float(input('Insira a quantidade gasta:\n'))
            gt += qtgast
            lz += qtgast
        elif tipo == 4:
            nomegasto = str(input('Insira o nome da despesa:\n')).title()
            g[nomegasto] = sum([float(input('Insira a quantidade gasta:\n'))])
    elif user == 2:
        #ainda pensando como configurar matplotlib
        print()
    elif user == 3:
        print('Saindo...')
        s(1)
        break


