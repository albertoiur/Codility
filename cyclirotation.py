# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 14:33:30 2017

@author: Rui
"""

def solution(A, K):
    """
    Right Rotation
    """
    
    tmp1 = tmp2 = []
    if len(A)==0:
        return A
    if len(A)==1:
        return A
    if K > len(A):
        valor_rotacao = K % len(A)
        tmp1 = A[(len(A)-valor_rotacao):]
        #print(tmp1)
        tmp2 = A[:len(A)-valor_rotacao]
        #print(tmp2)
        A = tmp1 + tmp2
    else:
        tmp1 = A[len(A)-K:]
        #print(tmp1)
        tmp2 = A[:len(A)-K]
        #print(tmp2)
        A = tmp1 + tmp2
    
    return A
    
    
    
#Teste
# n - numero de elementos da lista
# d - valor da rotação esquerda
# l - elementos da lista
print(solution([1,2],10001))
