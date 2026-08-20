import matplotlib.pyplot as plt
from time import sleep as s
from defs import limpador_de_tela, continuador, adicionar, tela_inicial, saidorsimples
import numpy as np

#as variáveis constantes do projeto:

sal = float(input('Salário:\n'))
limpador_de_tela()

ali = tp = lz = agua = luz = escola = internet = 0

g = {
    'Transporte': tp,
    'Alimentação': ali,
    'Lazer': lz,
    'Conta de luz': luz,
    'Internet': internet,
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
        tipo = int(input('[1]Transporte\n[2]Alimentação[3]Lazer\n[4]Conta de água\n[5]Conta de luz\n[6]Mensalidade escolar\n[7]Internet\n'))
        g = adicionar('Insira o valor gasto:\n', tipo=tipo, saldef=sal, dicionario=g)
        esc = continuador()
        if esc == 'n':
            saidorsimples()
            break

    #Opc mostra gráfico
    elif user == 2:

        porcentagens = np.array([100.0, *[ v / sal * 100 for k, v in g.items()]])
        nomes = ['Salário', 'Transporte', 'Alimentação', 'Lazer', 'Conta de água', 'Escola/Faculdade', 'Conta de luz', 'Conta de internet']
        plt.pie( porcentagens, labels=porcentagens)
        plt.legend(labels=nomes, loc='upper left', bbox_to_anchor=(-0.4, 1.1))
        plt.title('Porcentagem de gastos', loc='center')
        plt.show()
        break
    #Opc que muda o salário do usuário.

    elif user == 3:
        sal = float(input('Novo salário:\n'))
        esc = continuador()
        if esc == 'n':
            saidorsimples()
            break

    #Opc que termina a execução do programa.
    elif user == 4:
        limpador_de_tela()
        saidorsimples()
        break

    else:
        limpador_de_tela()
        print('Opção Invalida')


