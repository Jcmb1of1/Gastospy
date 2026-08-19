import matplotlib.pyplot as plt
from time import sleep as s
from defs import limpador_de_tela, continuador, adicionar, tela_inicial
import numpy as np

#as variáveis constantes do projeto:

sal = float(input('Salário:\n'))
limpador_de_tela()

ali = tp = lz = agua = luz = escola = internet = 0

g = {
    'Transporte': tp,
    'Aliimentação': ali,
    'Lazer': lz,
    'Conta de luz': luz,
    'Conta de internet': internet,
    'Conta de água': agua,
    'Escola/Faculdade': escola
}

while True:
    limpador_de_tela()
    tela_inicial()


    #escolha do usuário - o que ele quer fazer
    user = int(input('[1]Adicionar gastos\n[2]Ver gastos\n[3]Alterar salário\n[4]Sair do sistema\n'))


    #escolha do usuário - que gasto ele quer adicionar
    if user == 1:

        limpador_de_tela()
        print('Qual tipo de gasto?')

        # tipos de despesas
        tipo = int(input('[1]Transporte\n[2]Alimentação[3]Lazer\n[4]Conta de Luz\n[5]Conta de água\n[6]Mensalidade escolar\n[7]Internet'))

        if tipo == 1:
            limpador_de_tela()
            tp = adicionar('Insira a quantidade gasta\n', tp, sal)
            esc = continuador()
            if esc == 'n':
                break
        elif tipo == 2:
            limpador_de_tela()
            ali = adicionar('Insira a quantidade gasta\n', ali, sal)
            esc = continuador()
            if esc == 'n':
                break
        elif tipo == 3:
            limpador_de_tela()
            lz = adicionar('Insira a quantidade gasta\n', lz, sal)
            esc = continuador()
            if esc == 'n':
                break
        elif tipo == 4:
            limpador_de_tela()
            agua = adicionar('Insira a quantidade gasta\n', agua, sal)
            esc = continuador()
            if esc == 'n':
                break
        elif tipo == 5:
            limpador_de_tela()
            luz = adicionar('Insira a quantida gasta\n', luz, sal)
            esc = continuador()
            if esc == 'n':
                break
        elif tipo == 6:
            limpador_de_tela()
            escola = adicionar('Insira a quantidade gasta\n', escola, sal)
            esc = continuador()
            if esc == 'n':
                break
        elif tipo == 7:
            limpador_de_tela()
            internet = adicionar('Insira a quantida gasta\n', internet, sal)
            esc = continuador()
            if esc == 'n':
                break
    #Opc mostra gráfico
    elif user == 2:
        array = np.array([sal, tp, ali, lz, agua, escola, luz, internet])
        porcentagens = array/sal * 100
        nomes = ['Salário', 'Transporte', 'Alimentação', 'Lazer', 'Conta de água', 'Escola/Faculdade', 'Conta de luz', 'Conta de internet']
        plt.pie( porcentagens, labels=porcentagens)
        plt.legend(labels=nomes, loc='upper left', bbox_to_anchor=(-0.4, 1.1))
        plt.title('Porcentagem de gastos', loc='center')
        plt.show()
        break
    elif user == 3:
        sal = float(input('Novo salário:\n'))
        esc = continuador()
        if esc == 'n':
            break
    #Opc que termina a execução do programa.
    elif user == 4:
        limpador_de_tela()
        print('Saindo...')
        s(1)
        break
    else:
        limpador_de_tela()
        print('Opção Invalida')


