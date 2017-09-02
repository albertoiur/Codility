# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 15:30:52 2017

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