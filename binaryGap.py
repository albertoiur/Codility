# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 17:18:15 2017

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
        
def solution(N):
    tmp = bin(N)[2:]
    maximo = 0    
    minha_pilha = pilha()
    print('Binario: ',tmp)
    minha_pilha.push(tmp[0])
    for i in range(1,len(tmp)):
        conta = 0
        #print(i)
        #print(minha_pilha.mostra_pilha())           
        if tmp[i] == '0':
            minha_pilha.push(tmp[i])
        if tmp[i] == '1':
            while minha_pilha.peek() == '0':
                minha_pilha.pop()
                conta += 1
            if conta > maximo:
                maximo = conta
                
    return maximo               
    
print(solution(1041))    
       