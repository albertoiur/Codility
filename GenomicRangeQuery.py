# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 16:53:26 2017

@author: Rui
"""


def solution(S, P, Q):
    dados = {'A':1, 'C':2,'G':3, 'T':4}
    lista = []
    final = []
    indices = list(zip(P,Q))
    
    print('Indices: ', indices)
    lista = [dados[item] for item in S if item in dados]
           
    print('Lista: ',lista)
    """
    for k,v in indices:
        tmp = lista[k:v+1]
        print('TMP: ',tmp)
        tmp.sort()
        final.append(tmp[0])
    """
    for k,v in indices:
        tmp = tuple(lista[k:v+1])
        final.append(min(tmp))
        
    return final    

    
def solution2(S, P, Q):
    dados = {'A':1, 'C':2,'G':3, 'T':4}
    indices = tuple(zip(P,Q))
    
    #print('Indices: ', indices)
    lista = [dados[item] for item in S if item in dados]

    #tmp = [lista[k:v+1] for k,v in indices]
    tmp = list(map(lambda x : lista[x[0]:x[1]+1], indices))
    #final = [ min(item) for item in tmp]
    final = list(map(lambda item: min(item), tmp))
    return final       
    
    

S = 'CAGCCTA'
P = [2,5,0]   
Q = [4,5,6] 
print(solution2(S,P,Q))