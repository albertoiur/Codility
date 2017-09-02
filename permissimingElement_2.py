# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 14:47:54 2017

@author: Rui
"""

class pilha:
    
    #Sempre que a classe Pilha é chamada cria uma lista vazia (vector)
    def __init__(self):
        self.vector = []
    #Se pilha 'lista vector' é vazia, retorna True senão False
    def isempty(self):
        return self.vector == []
    #Inserir elemnto no topo da pilha (fim da lista)
    def push(self,elemento):
        self.vector.append(elemento)
    #Elimina o elemento do topo da pilha (último elemnto da lista)    
    def pop(self):
        return self.vector.pop()
    #Retorna o tamanho da pilha    
    def size(self):
        return len(self.vector)
    #Retorna o elemnto no topo da pilha    
    def peek(self):
        return self.vector[len(self.vector) - 1]
    #Apresenta o conteúdo da pilha (lista vector)                       
    def mostra_pilha(self):
        return self.vector
        
        
def solution(A):
    tmp = set(A)
    A = list(tmp)
    minha_pilha = pilha()
            
    A.sort()
    minha_pilha.push(1)
    
    for item in A:
        if item < 1:
            continue
        if item == minha_pilha.peek():
            x = minha_pilha.peek() 
            minha_pilha.push(x + 1)
        else:
            return minha_pilha.peek()
    return minha_pilha.peek()       
        
        
        
            
A =  []  
print(solution(A))              
                
        