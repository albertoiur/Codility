# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 17:09:15 2017

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

    def peek_bottom(self):
        return self.vector[0]
    #Apresenta o conteúdo da pilha (lista vector)                       
    def mostra_pilha(self):
        return self.vector
        
    def inserir_lista(self,lista):
        self.vector.extend(lista)
        
def solution(A):
    pilha_num1 = pilha()
    pilha_nim2 = pilha()
    
    pilha_num1.inserir_lista(A)
    print(pilha_num1.mostra_pilha())    
    return pilha_num1.peek_bottom()


print(solution([-3,1,2,-2,5,6]))    
    
    
        