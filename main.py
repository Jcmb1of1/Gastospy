import numpy as np
import matplotlib.pyplot as plt
import datetime


#todas as variáveis constantes do projeto:

sal = float(input('Salário:\n'))

gf = {

}
#gastos fixos


ali, tp, lz, gt = [], [], [], []
#alimentação, transporte, lazer, gastos totais


while True:
    #tela inicial
    print('GERENCIADOR DE GASTOS SIMPLES')


    #escolha do usuário - o que ele quer fazer
    user = int(input('[1]Adicionar gastos\n[2]Ver gastos\n[3] Sair do sistema'))


    #escolha do usuário - que gasto ele quer adicionar
    if user == 1:
        print('Qual tipo de gasto?')
        tipo = int(input('[1]Transporte\n[2]Alimentação\n[3]Lazer\n[4]Gastos Fixos'))
        if tipo == 1:
            qtgast = float(input('Insira a quantidade gasta:\n'))
            tp.append(qtgast)
            gt.append(qtgast)
        elif tipo == 2:
            qtgast = float(input('Insira a quantidade gasta:\n'))
            ali.append(qtgast)
            gt.append(qtgast)

