# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 11:14:58 2017

@author: Rui



Write a function:

    def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible 
by K, i.e.:

    { i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers 
divisible by 2 within the range [6..11], namely 6, 8 and 10.

Assume that:

        A and B are integers within the range [0..2,000,000,000];
        K is an integer within the range [1..2,000,000,000];
        A ≤ B.

Complexity:

        expected worst-case time complexity is O(1);
        expected worst-case space complexity is O(1).


"""

def solution(A,B,K):
    conta = 0
    for i in range(A,B+1):
        if i % K == 0:
            conta += 1
    return conta        

def solution_2(A,B,K):
    if A%K == 0:
        valor = 1
    else:
        valor = 0
    
    return B//K - A//K + valor
        
#print(solution_2(6,11,2))     
print(solution_2(11,345,17))    