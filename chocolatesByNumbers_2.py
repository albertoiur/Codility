# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 17:00:33 2017

@author: Rui
"""

def hashing_fun(x,N,M):
    x = x  + M
    if x >= N:
        while x >= N:
            x = x - N
    return x

def solution(N,M):
    x = 0   
    table = [1] * N
    conta = 1
    table[0] = 0

    if len(table)==1:
        return 1
   
    for i in range(N):
        x = hashing_fun(x,N,M)        
        #print(x)
        if table[x] == 1:
            table[x] = 0
            conta += 1
        else:
            return conta
            
            
def solution_2(N,M):
    dados = dict()
    x=0
    for i in range(N):
        dados[i] = 1

    dados[0] = 1
    conta = 0
    
    while True:
        x = hashing_fun(x,N,M)
        if dados[x] == 1:
            dados[x] = 0
            conta += 1
        else:
            return conta
    
    
            
            
            
            
            

      
print(solution_2(1,2))    