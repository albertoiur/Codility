# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 21:14:37 2017

@author: Rui
"""

def solution(A):
    minimo = sum(A)
    
    for i in range(len(A) - 1):
        head = A[0:i+1]
        tail = A[i+1:]
        tmp = abs(sum(head) - sum(tail))
        if tmp < minimo:
            minimo = tmp
            
    return minimo       
    
print(solution([3,1,2,4,3]))    