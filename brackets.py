# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 21:31:08 2017

@author: Rui

CODILITY TEST - STACKS
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
        
        
def match(abrir,fechar):
    abertos = '([{'
    fechados = ')]}'
    
    return abertos.index(abrir) == fechados.index(fechar)

    
        
        
def solution(S):
    #criar pilha vazia
    minha_pilha = pilha()
     
    #percorrer toda a strin da esq. para a direita
    for item in S:
        if item in '({[':
            minha_pilha.push(item)
        else:
            if minha_pilha.isempty():
                return 0
            else:
                if match(minha_pilha.peek(),item):
                    minha_pilha.pop()
    
    if minha_pilha.isempty():
        return 1
    else:
        return 0
     
        
        
#A = '([)()]'
A = "{[()()]}" 
print(solution(A))   