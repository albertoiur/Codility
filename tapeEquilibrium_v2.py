# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 16:05:34 2017

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
        
    def push_head(self,elemento):
        self.vector.insert(0,elemento)
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
       
    def soma_pilha(self):
        return sum(self.vector)
        
    def add_lista(self,lista):
        self.vector.extend(lista)
 
        
def solution(A):
    pilha1 = pilha()
    pilha2 = pilha()
    pilha3 = pilha()
    
    pilha1.add_lista(A)
    soma_p1 = pilha1.soma_pilha()
    soma_p2 = 0
    while pilha1.size() > 1:
        x = pilha1.pop()
        #print('X = ',x)
        pilha2.push(x)
        #print(pilha2.mostra_pilha())
        #soma_pilha1 = pilha1.soma_pilha()
        soma_p1 = soma_p1 - x
        #print(soma_pilha1)
        soma_p2 = soma_p2 + x
        #print(soma_pilha2)
        resultado = (soma_p2 - soma_p1)
        if pilha3.size() > 0:
            if abs(resultado) < pilha3.peek():
                pilha3.pop()
                pilha3.push(abs(resultado))
        else:
            pilha3.push(abs(resultado))
            
    return pilha3.peek()       

print(solution([-10,-5,-3,-4,-5])) 
#print(solution([-1000,1000]))
#print(solution([3,1,2,4,3]))       