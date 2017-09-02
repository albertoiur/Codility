# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 18:46:30 2017

@author: Rui
"""

def binaryGap(num):
    """
    A binary gap within a positive integer N is any maximal sequence of consecutive 
    zeros that is surrounded by ones at both ends in the binary representation of N.
    For example, number 9 has binary representation 1001 and contains a binary gap
    of length 2. The number 529 has binary representation 1000010001 and contains
    two binary gaps: one of length 4 and one of length 3. The number 20 has binary 
    representation 10100 and contains one binary gap of length 1. The number 15 has
    binary representation 1111 and has no binary gaps.
    """
    valor = bin(num)[2:]
    print('O num {} em binário é gual a {}.'.format(num,valor))
    total = conta = 0
    
    for i in valor:
        if i == '1':
            conta = 0
        elif i=='0':
            conta = conta +1
            if conta > total:
                total = conta
                
    return total        




def oddOcurrencysinArray(A):
    for item in A:
        valor = A.count(item)
        if valor == 1:
            return item
    


def oddOcurrencysinArray_v2(A):
    d = {}

    for item in A:
        if item not in d:
            d[item] = 1
        else:
            d[item] += 1

    for k,v in d.items():
        if v == 1:
            return k

def Frogjmp(x,y,d):
    """
    For example, given:
    X = 10
    Y = 85
    D = 30

  the function should return 3, because the frog will be positioned as follows:

        after the first jump, at position 10 + 30 = 40
        after the second jump, at position 10 + 30 + 30 = 70
        after the third jump, at position 10 + 30 + 30 + 30 = 100


    """
        
    conta = 0
    while (x < y):
        x = x + d
        conta += 1
    return conta
    
    

def Frogjmp_v2(X,Y,D):
    tmp = Y - X
    if tmp % D == 0:
        return tmp / D
    else:
        v = int(tmp / D) + 1
        return int(v)


def PermMissingElement(A):
    """
    For example, given array A such that:
  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5

the function should return 4, as it is the missing element.

Assume that:

        N is an integer within the range [0..100,000];
        the elements of A are all distinct;
        each element of array A is an integer within the range [1..(N + 1)].
    """
 
    n = len(A) + 1
    sum_a = sum(A)
    sum_total = (n * (n+1)) // 2
    return sum_total - sum_a
    

 
 
    
    
def dominator(A):
    """
    A[0] = 3    A[1] = 4    A[2] =  3
    A[3] = 2    A[4] = 3    A[5] = -1
    A[6] = 3    A[7] = 3

    the function may return 0, 2, 4, 6 or 7, as explained above.
    """
    d = {}
    resultado = []

    for item in A:
        if item not in d:
            d[item] = 1
        else:
            d[item] += 1

    lista = sorted(d.items(), key = lambda t : t[1], reverse = True)
    #print(lista)
    x = lista[0][0]
    vezes = lista[0][1]
    #print(x)
    if vezes < (len(A)//2):
        return -1
    

    for item in range(len(A)):
        if A[item] == x:
            resultado.append(item)
    
    for f in resultado:
        print(' {}, '.format(f))
    

        
        
        
def dominator_v2(A):
    
    candidate_ele = ''
    candidate_cnt = 0
     
    for value in A:
        if candidate_ele == '':
            candidate_ele = value
            candidate_cnt = 1
        else:
            if value != candidate_ele:
                candidate_cnt -= 1
                if candidate_cnt == 0:
                    candidate_ele = ''
            else:
                candidate_cnt += 1
         
    if candidate_cnt == 0:
        return -1
         
    cnt = 0
    last_idx = 0
     
    for idx, value in enumerate(A):
        if value == candidate_ele:
            cnt += 1
            last_idx = idx
             
    if cnt > len(A)//2:
        return last_idx
         
    return -1

  
def PermMissingElement_v2(A):
    lista = set(A)
    A = list(lista)
    A.sort()
    if len(A)== 1 and A[0] > 0:
        return A[0] + 1
        
    for i in range(min(A), max(A)):
        if i <= 0:
            continue
        elif i in A:
            continue
        else:
            return i
    return 1
    
   
def ciclyRotation(A,K):
    """
    A zero-indexed array A consisting of N integers is given. Rotation of the array means that each 
    element is shifted right by one index, and the last element of the array is also moved to the first
    place.

    For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7]. The goal is to rotate 
    array A K times; that is, each element of A will be shifted to the right by K indexes.
    """
    if len(A) == 1:
        return A
    tmp = [0] * len(A)
    for i in range(len(A)):
        if i+K < len(A):
            tmp[i+K] = A[i]
        else:
            x = (i+K) - len(A)
            print(x)
            tmp[x] = A[i]

    return tmp
            

def count_div(A, B, K):
    """
    Returns the number of integers within the range [A..B] that are divisible by K.  
    Args:
      - A: is an integer within the range [0..2,000,000,000]
      - B: is an integer within the range [0..2,000,000,000] and A <= B
      - K: is an integer within the range [1..2,000,000,000]
    """
    conta = 0
    for item in range(A, B+1):
        if item % K == 0:
            conta +=1
    return conta        
    
    
 
#Maximum Slice Problem

def MaxSliceSum(A):
    """
    Resultado obtido = 100%
    
    A non-empty zero-indexed array A consisting of N integers is given. A pair of integers (P, Q), 
    such that 0 ≤ P ≤ Q < N, is called a slice of array A. The sum of a slice (P, Q) is the total 
    of A[P] + A[P+1] + ... + A[Q].
    Write a function:
        def solution(A)

    that, given an array A consisting of N integers, returns the maximum sum of any slice of A.
    
    Algoritmo Kadane's
    """
    max_ate_agora = A[0]  
    max_actual = A[0]  

    for i in range(1,len(A)):
        max_actual = max(A[i], max_actual+A[i])
        max_ate_agora = max(max_ate_agora, max_actual)
        
    return max_ate_agora    
    
    
def MaxProfit(A):
    """
    A zero-indexed array A consisting of N integers is given. It contains daily prices of a stock 
    share for a period of N consecutive days. If a single share was bought on day P and sold on day Q,
    where 0 ≤ P ≤ Q < N, then the profit of such transaction is equal to A[Q] − A[P], provided 
    that A[Q] ≥ A[P]. Otherwise, the transaction brings loss of A[P] − A[Q].

    For example, consider the following array A consisting of six elements such that:
      A[0] = 23171
      A[1] = 21011
      A[2] = 21123
      A[3] = 21366
      A[4] = 21013
      A[5] = 21367

    If a share was bought on day 0 and sold on day 2, a loss of 2048 would occur because 
    A[2] − A[0] = 21123 − 23171 = −2048. If a share was bought on day 4 and sold on day 5, a profit of 
    354 would occur because A[5] − A[4] = 21367 − 21013 = 354. Maximum possible profit was 356. It 
    would occur if a share was bought on day 1 and sold on day 5.

    Write a function, 
    def solution(A)

    that, given a zero-indexed array A consisting of N integers containing daily prices of a stock 
    share for a period of N consecutive days, returns the maximum possible profit from one transaction 
    during this period. The function should return 0 if it was impossible to gain any profit.

    For example, given array A consisting of six elements such that:
      A[0] = 23171
      A[1] = 21011
      A[2] = 21123
      A[3] = 21366
      A[4] = 21013
      A[5] = 21367
    
    the function should return 356, as explained above.
    """
    max_profit = 0
    min_day = 200000
     
    for item in A:
        min_day = min(min_day, item)
        max_profit = max(max_profit, item - min_day)
     
    return max_profit
  
    
    
      
    
    
    
    
#Testes
#print(binaryGap(1041))  
#print(oddOcurrencysinArray_v2([9,3,9,3,9,7,9])) 
#print(Frogjmp_v2(10,85,30))
#print(PermMissingElement_v2([1]))
#print(dominator_v2([3,4,3,2,3,-1,3,3]))
#print(ciclyRotation([1, 1, 2, 3, 5], 5))
#print(count_div(1, 20000, 1000))
#print(MaxSliceSum([3,2,-6,4,0]))
print(MaxProfit([23171,21011,21123,21366,21013,21367]))