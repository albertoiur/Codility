# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 14:31:53 2017

@author: Rui
"""

def solution(A):
    conta = 0
    
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i]==0:
                if A[j] == 1:
                    conta += 1
            else:
                continue
    if conta > 1000000000:
        return -1
    else:
        return conta

print(solution([1,0,1,1,1]))        