# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 20:59:53 2017

@author: Rui
"""

def solution(A):
    if len(A) < 3:
        raise Exception("Invalid input")
         
    A.sort()
     
    return max(A[0] * A[1] * A[-1], A[-1] * A[-2] * A[-3])
  
def solution_2(A):
    A = sorted(A)
    return max(A[-1] * A[-2] * A[-3], A[0] * A[1] * A[-1])    
    
lista = [-3,1,2,-2,5,6]    
print(solution_2(lista))