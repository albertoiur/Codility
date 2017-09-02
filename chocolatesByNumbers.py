# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 15:15:48 2017

@author: Rui
"""

class deque():
    def __init__(self):
        self.vector = []

    def addFront(self,item):
        self.vector.insert(0,item)
        
    def addRear(self,item):
        self.vector.append(item)
        
    def removeFront(self):
        return self.vector.pop(0)
        
    def removeRear(self):
        return self.vector.pop()
        
    def removeFrontnTimesAddRear(self,n):
        for i in range(n):
            x = self.removeFront()
            self.addRear(x)
            
    def updateFront(self,x):
        self.vector[0] = x
        
        
    def isempty(self):
        return self.vector == []

    def size(self):
        return len(self.vector)
        
    def mostra_deque(self):
        return self.vector
        
    def mostra_front(self):
        return self.vector[0]

    def criar_fila(self,lista):
        self.vector.extend(lista)
        
        
def solution(N, M):
    conta = 0
    caixa_chocolates = deque()
    
    A = [1] * N

    caixa_chocolates.criar_fila(A)
    
    while caixa_chocolates.mostra_front() != 0:
        caixa_chocolates.updateFront(0)
        conta += 1
        caixa_chocolates.removeFrontnTimesAddRear(M)
        
    return conta    
        

       
print(solution(1,2))    
    

    
        