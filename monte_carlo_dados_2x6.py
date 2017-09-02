# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 22:00:30 2016

@author: ruialberto

Programa:
    - Monte Carlo Simulação
    - Qual a probabilidade de sair dois 6 num jogo (dados) de 24 tentativas?

"""

import random

def lancardado():
    valor = random.randint(1,6)
    return valor


def simular(numvezes):

    vitorias = 0

    for f in range(numvezes):
        for i in range(24):
            d1 = lancardado()
            d2 = lancardado()
            if d1 == 6 and d2 == 6:
                vitorias += 1
                break


    resultado = vitorias / numvezes

    return resultado

print('Probabilidade de sair 2 seis: ', simular(100))
