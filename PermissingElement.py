# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 14:43:57 2017

@author: Rui
"""

def solution(A):
    
    
    if len(A)==0:
        return 1
        
    if len(A)==1 and A[0]== 1:
        return 2
        
    if len(A) == 1:
        return A[0] - 1
    
    A.sort()
    
    if len(A)== A[-1]:
        return A[-1] + 1

    conta = A[0]
    
    

    for i in A:
        if i == conta:
            conta += 1
        else:
            return conta
    return A[0] - 1        

print(solution([5,4]) )          