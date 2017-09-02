# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 21:17:36 2017

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
    minha_pilha = pilha()
    A.sort()
    conta = 0
    
    minha_pilha.push(1)
    minha_pilha.mostra_pilha()        
    while conta <= len(A)-1:
        if A[conta] == minha_pilha.peek():
            x = minha_pilha.peek() + 1    
            minha_pilha.push(x)
            conta += 1
        else:
            return 0        
             
    return 1    
        
print(solution([4,1,3,2]))    