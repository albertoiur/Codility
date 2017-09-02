# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 15:32:55 2017

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
        
    def isempty(self):
        return self.vector == []

    def size(self):
        return len(self.vector)
        
    def mostra_deque(self):
        return self.vector

def solution(A, K):
    fila = deque()
    
    if A == []:
        return A
        
    for e in A:
        fila.addRear(e)
     
        
    for i in range(K):
        ultimo = fila.removeRear()
        fila.addFront(ultimo)
        
    return fila.mostra_deque()    
        
print(solution([],5))    