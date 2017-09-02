# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 20:38:22 2017

@author: Rui
"""

def MissingInteger(A):
    """
    Find the minimal positive integer not occurring in a given sequence.
    Execution: You only need to consider the first (N) positive integers. 
               In this specification 0 does not count as a valid candidate! 
               Any value that is below 1 or above N can be ignored.
    """
    seen = [False] * len(A)
    #print(seen)
    for value in A:
        #if 0 < value <= len(A):
        if value > 0 and value <= len(A):
            seen[value-1] = True
            print(seen)
 
    for idx in range(len(seen)):
        if seen[idx] == False:
            #print('**** - ',idx +1)
            return idx + 1
 
    return len(A)+1


print(MissingInteger([1,2,3,100,101,103]))

           