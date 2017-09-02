# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 23:21:57 2016

@author: ruialberto

Programa:
    ---------------------------------------------------------
    - Monte Carlo Simulação                                 -
    ---------------------------------------------------------
    - Qual a probabilidade de sair dois 6 num jogo (dados) de 24 tentativas?
    - Qual o lucro/prejuizo aposta de 5.0€
"""

import random

def lancardado():
    valor = random.randint(1,6)
    return valor
    
    
def simular(numvezes):
  
    vitorias = 0
    lucro = 0.0
        
    for f in range(numvezes):
        print ('Jogo nº: ', f+1)        
        for i in range(24):
            d1 = lancardado()
            print('dado 1: ',d1)
            d2 = lancardado()
            print('dado 2: ',d2)
            if d1 == 6 and d2 == 6:
                vitorias += 1
                break
            
                
    #resultado = vitorias / numvezes
    lucro = float((vitorias*5.0) - ((numvezes-vitorias)*5.0))
    
    #return resultado, lucro
    return lucro
    
print('Lucro/Prejuizo jogo dados (2 x seis): ', simular(10)) 
