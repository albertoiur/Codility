# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 17:42:28 2017

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
    
def solution(A):
    conta = 0    
    i = 1
    try:
        lider = calcula_dominator(A)
    except:
        return 0
    for item in range(len(A)):
        head = A[:i]
        tail = A[i:]
        print('Head: ',head)
        print('Tail: ',tail)
        num_vezes_leader_head = head.count(lider)
        num_vezes_leader_tail = tail.count(lider)
        if num_vezes_leader_head > len(head) // 2 and num_vezes_leader_tail > len(tail) // 2:
            conta += 1
        i += 1
            
    return conta        
            
    
    
    
    
    
    
    
    
    
    
#print(solution([4,3,4,4,4,2]))
#print(solution([0,0,0,0,1,0]))
print(solution([1,2]))  