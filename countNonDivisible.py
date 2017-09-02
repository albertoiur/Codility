# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 22:09:04 2017

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
        
    def criar_fila(self,lista):
        self.vector.extend(lista)
        
def solution(A):
    conta = 0
    resultado = list()
    fila = deque()
    fila.criar_fila(A)
    contador = 0
    
    while contador < len(A):
        contador += 1
        x = fila.removeFront()
        fila.addRear(x)
        #print(x)
        vector = fila.mostra_deque()
        for i in vector:
            if x % i != 0:
                conta += 1
                #print(conta)
        resultado.append(conta)
        conta=0
    return resultado        
                
print(solution([3,1,2,3,6]))            