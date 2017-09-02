# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 16:56:36 2017

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
        
        
def solution(H):
    conta = 0
    blocos = pilha()
    
    for item in H:
        altura = 0
        while(blocos.size()>0):
            altura = blocos.peek()
            if altura > item:
                blocos.pop()
            else:
                break
        if altura != item:
            blocos.push(item)
            conta += 1
            
    return conta

print(solution([8,8,5,7,9,8,7,4,8]))        
        