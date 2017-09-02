# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 17:03:05 2017

@author: Rui
"""

def solution(X, Y, D):
    
    
    if Y < X or D <= 0:
        raise Exception("Argumentos invalidos")
         
    if (Y- X) % D == 0:
        return (Y- X) // D
    else:
        return ((Y- X) // D) + 1
    
print(solution(10,85,30))    


