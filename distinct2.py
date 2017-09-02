# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 21:51:45 2017

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
    #Criar uma lista vazia
    
    new_list = pilha()
    A.sort()
    if len(A) == 0:
        return 0
    new_list.push(A[0])
    for item in range(1,len(A)):
        if A[item] != new_list.peek():
            new_list.push(A[item])
    return new_list.size()    
        
A = [2,1,1,2,3,1] 
print(solution(A))   