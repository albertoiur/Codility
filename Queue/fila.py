# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 14:23:19 2017

@author: Rui
"""

class fila:
    def __init__(self):
        self.vector = []

    def enqueue(self,item):
        self.vector.append(item)
        
    def dequeue(self):
        return self.vector.pop(0)
        
    def isempty(self):
        return self.vector == []

    def size(self):
        return len(self.vector)
        
    def mostrar_fila(self):
        return self.vector

    