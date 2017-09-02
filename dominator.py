# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 16:44:28 2017

@author: Rui
"""

def calcula_dominator(A):
    dados = {}

    for item in A:
        if item not in dados:
            dados[item] = 1
        else:
            dados[item] += 1

    tamanho = len(A) // 2

    for k,v in dados.items():
        if v > tamanho:
            x = k
            
    return x


def soluction(A):
    final = []
    try:
        x = calcula_dominator(A)
    except:
        return -1
    
    final = [item for item in range(len(A)) if A[item]==x]    
    
    return final[-1]
        
        
    
    
    
print(soluction([3,4,3,2,3,-1,3,3]))    
#print(soluction([3,4])) 
