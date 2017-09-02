# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 20:55:58 2017

@author: Rui
"""

def solution(S):
    quadro = [0] * len(S)
    tamanho = len(S)
    if len(S)==1:
        return 0
    for i in range(len(S)//2):
        if S[i] == S[tamanho - 1]:
            quadro[i] = 1
            quadro[tamanho - 1] = 1
            tamanho -= 1
    
    #print('Quadro: ',quadro)        
    if quadro.count(0) == len(S):
        return -1
        
    if 0 in quadro:
        return quadro.index(0)
    else:
        return -1
             
            
print(solution('abxcba'))            