# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 16:19:42 2017

@author: Rui
"""

def solution(A):
    lucro_tmp = 0
    lucro_max = 0
    
    for item in range(1,len(A)):
        lucro_tmp = max(0,lucro_tmp + (A[item]-A[item-1]))
        lucro_max = max(lucro_max, lucro_tmp)
    return lucro_max     


def max_slice(A):
    max_ending = max_slice = 0
    
    for a in A:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice,max_ending)
    return max_slice    






print(max_slice([1,5,3,4,7]))    
#print(solution([23171]))    