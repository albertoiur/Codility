# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 14:33:26 2017

@author: Rui
"""

class arvoreBinaria():
    def __init__(self,chave):
        self.chave = chave
        self.lado_esquerdo = None
        self.lado_direito = None
        
    def inserir_esquerda(self,valor):
        if self.lado_esquerdo == None:
            self.lado_esquerdo = arvoreBinaria(valor)
        else:
            t = arvoreBinaria(valor)
            t.lado_esquerdo = self.lado_esquerdo
            self.lado_esquerdo = t
            
    def inserir_direita(self,valor):
        if self.lado_direito == None:
            self.lado_direito = arvoreBinaria(valor)
        else:
            t = arvoreBinaria(valor)
            t.lado_direito = self.lado_direito
            self.lado_direito = t
            
    def get_lado_esquerdo(self):
        return self.lado_esquerdo
        
    def get_lado_direito(self):
        return self.lado_direito
        
    def get_raiz(self):
        return self.chave
        
    def actualizar_raiz(self,valor):
        self.chave = valor


        
"""            
r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal()) 
"""           