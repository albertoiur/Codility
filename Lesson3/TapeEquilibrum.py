# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 16:57:36 2017

@author: Rui



A non-empty zero-indexed array A consisting of N integers is given. Array A represents
numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty 
parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value 
of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and 
the sum of the second part.

For example, consider array A such that:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3

We can split this tape in four places:

        P = 1, difference = |3 − 10| = 7
        P = 2, difference = |4 − 9| = 5
        P = 3, difference = |6 − 7| = 1
        P = 4, difference = |10 − 3| = 7

Write a function:

    def solution(A)

that, given a non-empty zero-indexed array A of N integers, returns the minimal difference that can be achieved.

For example, given:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3

the function should return 1, as explained above.

Assume that:

        N is an integer within the range [2..100,000];
        each element of array A is an integer within the range [−1,000..1,000].

Complexity:

        expected worst-case time complexity is O(N);
        expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.

"""

def solution(A):
    minimo = abs(A[0] - sum(A[1:]))
    if A==[]:
        return 0
    
    for i in range(len(A)-1):
        head = A[:i+1]
        #print('HEAD: ', head)
        tail = A[i+1:]
        #print('TAIL: ', tail)
        dif = abs(sum(head) - sum(tail))
        #print(dif)
        if dif < minimo:
            minimo = dif
    return minimo

    
    
def solution_2(A):
    minimo = abs(A[0] - sum(A[1:]))
    if A==[]:
        return 0
    head  = list()
    tail = list()
    head.append(A[0]) 
    tail=A[1:]
    #print('head:',head)
    #print('tail:',tail)
    while len(tail) > 0:
        soma_head = sum(head)
        soma_tail = sum(tail)
        dif = abs(soma_head - soma_tail)
        if dif < minimo:
            minimo = dif
        head.append(tail.pop(0)) 
    return minimo








lista = [3,1,2,4,3]    
#lista = [-1000,1000]    
print(solution_2(lista))    
