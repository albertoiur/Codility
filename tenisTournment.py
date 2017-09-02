# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 18:16:10 2017

@author: Rui
"""

def solution(P, C):
    if P == 0 or C == 0:
        return 0
        
    qtos_pares_jogadores = P // 2
    
    if qtos_pares_jogadores >= C:
        return C
    else:
        return qtos_pares_jogadores

        
print(solution(10,3))