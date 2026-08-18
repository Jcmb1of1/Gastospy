import matplotlib.pyplot as plt
from datetime import date
from time import sleep as s
from defs import limpador_de_tela, continuador

#as variáveis constantes do projeto:

sal = float(input('Salário:\n'))
limpador_de_tela()

ali = tp = lz = gt = agua = luz = escola = internet = 0

g = {
    'Transporte': tp,
    'Aliimentação': ali,
    'Lazer': lz,
    'Gastos totais': gt,
    'Conta de luz': luz,
    'Conta de internet': internet,
    'Conta de água': agua,
    'Escola/Faculdade': escola
}

while True:
    limpador_de_tela()
    print(date.today())
    #tela inicial
    print('GERENCIADOR DE GASTOS SIMPLES')


    #escolha do usuário - o que ele quer fazer
    user = int(input('[1]Adicionar gastos\n[2]Ver gastos\n[3]Sair do sistema\n'))


    #escolha do usuário - que gasto ele quer adicionar
    if user == 1:
        limpador_de_tela()
        print('Qual tipo de gasto?')
        tipo = int(input('[1]Transporte\n[2]Alimentação\n'))
        if tipo == 1:
            limpador_de_tela()
            qtgast = float(input('Insira a quantidade gasta:\n'))
            tp += qtgast
            gt += qtgast
            esc = continuador()
            if esc == 'n':
                break
        elif tipo == 2:
            limpador_de_tela()
            qtgast = float(input('Insira a quantidade gasta:\n'))
            gt += qtgast
            ali += qtgast
            esc = continuador()
            if esc == 'n':
                break
        elif tipo == 3:
            limpador_de_tela()
            qtgast = float(input('Insira a quantidade gasta:\n'))
            gt += qtgast
            lz += qtgast
            esc = continuador()
            if esc == 'n':
                break

    elif user == 2:
        #ainda pensando como configurar matplotlib
        porcentagens = [sal/sal * 100, tp/sal * 100, ali/sal * 100, lz/sal * 100, agua/sal*100, escola/sal*100, luz/sal*100, internet/sal*100 ]
        nomes = ['Salário', 'Transporte', 'Alimentação', 'Lazer', 'Conta de água', 'Escola/Faculdade', 'Conta de luz', 'Conta de internet']
        plt.pie( porcentagens, labels=porcentagens)
        plt.legend(labels=nomes, loc='upper left', bbox_to_anchor=(-0.4, 1.1))
        plt.show()
        print()
    elif user == 3:
        print('Saindo...')
        s(1)
        break


