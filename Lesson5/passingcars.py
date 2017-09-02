# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 12:11:25 2017

@author: Rui
"""

def solution(A):
    pares = 0
    total = 0
    for i in range(len(A)):
        if A[i] == 0:
            total += 1
        elif A[i] == 1:
            pares += total
            if pares > 1000000000:
                return -1
    return pares            