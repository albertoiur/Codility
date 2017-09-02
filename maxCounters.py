# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 22:06:15 2017

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

def solution(N, A):
    resultado = [0] * N
    minha_pilha = pilha()
    minha_pilha.push(0)
    for i in range(len(A)):
        if A[i] >= 1 and A[i] <= N:
            resultado[A[i]-1] += 1
            if resultado[A[i]-1] > minha_pilha.peek():
                minha_pilha.pop()
                minha_pilha.push(resultado[A[i]-1])
        else:
            resultado = [minha_pilha.peek()] * N
    return resultado 


print(solution(5,[3,4,4,6,1,4,4]))       