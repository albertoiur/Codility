# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 16:08:02 2017

@author: Rui
"""

class pilha:
    
    #Sempre que a classe Pilha é chamada cria uma lista vazia (vector)
    def __init__(self):
        self.vector = []
    #Se pilha 'lista vector' é vazia, retorna True senão False
    def isempty(self):
        return self.vector == []

    #Verifica se elemento já existe na pilha
    def exist(self,elemento):
        if elemento in self.vector:
            return True
        else:
            return False
            
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
        
        
def solution(X, A):
    minha_pilha = pilha()
    
    for i in range(len(A)):
        if minha_pilha.size() >= (X-1):
            if A[i] == X:
                return i
            else:
                continue
        else:
            if minha_pilha.exist(A[i]) or A[i] == X:
                continue
            else:
                minha_pilha.push(A[i])
                print(minha_pilha.mostra_pilha())
    return -1
    
    
  
#print(solution(5,[1,3,1,4,2,3,5,4]))
#print(solution(5,[1,5,3,1,4,2,3,5,4]))
#print(solution(3, [1, 3, 1, 3, 2, 1, 3]))    


     