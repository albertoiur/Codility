# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 21:27:59 2017

@author: ruialberto
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
    #Fundo da pilha    
    def head(self):
        return self.vector[0]
        
    def anterior_ao_topo(self):
        return self.vector[len(self.vector) - 2]
        
        
def solution(A):
    minha_pilha = pilha()
    A.sort()
    
    minha_pilha.push(A[0])
    for item in range(1,len(A)):
        minha_pilha.push(A[item])
        if minha_pilha.size() == 1:
            continue
        if minha_pilha.peek() == minha_pilha.anterior_ao_topo():
            minha_pilha.pop()
            minha_pilha.pop()
    
    return minha_pilha.peek()        
        
        
print(solution([9,3,9,3,9,7,9]))        
        