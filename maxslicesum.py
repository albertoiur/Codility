# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 15:38:56 2017

@author: Rui
"""

        

        
def solution(A):
   maximo_tmp = A[0]
   maximo = A[0]
   for item in A[1:]:
       maximo_tmp = max(item, maximo_tmp+item)
       maximo = max(maximo,maximo_tmp) 
   return maximo    
        
        
        
#print(solution([23,3,45,12]))
#print(solution([3,2,-6,4,0]))
print(solution([1,1,1]))         