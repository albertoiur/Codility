# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 14:17:50 2017

@author: Rui
"""

def solution(A):
    mais_alto = 0
    mais_baixo = 0
    resultado = 0
    
    for i in A:
        if i >= mais_alto:
            resultado = max(resultado, mais_alto - mais_baixo)
            mais_alto = mais_baixo = i
        elif i < mais_baixo:
            mais_baixo = i
            
        elif i > mais_baixo:
            resultado = max(resultado, i - mais_baixo)
            
    return resultado

print(solution([4,3]))        