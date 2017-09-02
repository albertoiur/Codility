# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 16:36:29 2017

@author: Rui

A = [4,3,2,1,5] - Peso dos peixes
B = [0,1,0,0,0] - 0 = Up stream, 1 = Down Stream
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
                           
        
def solution(A, B):
    nova_pilha = pilha()
    
    nova_pilha.push(B[0])
    for item in range (1,len(B)):
        anterior = nova_pilha.peek()
        nova_pilha.push(B[item])
        if nova_pilha.peek() == 0 and anterior == 1:
            nova_pilha.pop()
    return nova_pilha.size()        
            
        
              
    
    
       
#A = [4,3,2,1,5] 
#B = [0,1,0,0,0] 
A = [5,4,23,1] 
B = [0,0,1,1] 
print(solution(A,B))    