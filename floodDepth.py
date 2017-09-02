# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 22:14:30 2017

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

    def bottom(self):
        return self.vector[0]
    #Apresenta o conteúdo da pilha (lista vector)                       
    def mostra_pilha(self):
        return self.vector
        
    def clear_all(self):
        self.vector = []
        
       
def solution(A):
    nova_pilha = pilha()
    lista = []
    final = []
    tamanho = len(A)
    
    
    if tamanho >= 0 and tamanho < 3:
        return 0
        
    nova_pilha.push(A[0]) 
    
    for item in range(1,len(A)):        
        if A[item] <= nova_pilha.bottom():
            nova_pilha.push(A[item])            
        #lista.append(A[item])
        """
        while not nova_pilha.isempty():
            lista.append(nova_pilha.pop())
        print(lista)
        """
        lista.extend(nova_pilha.mostra_pilha())
        print(lista)
        nova_pilha.clear_all()        
        if lista[0] == lista[-1]:
           valor = lista[0] - min(lista)
        else:
           valor = max(lista[1:]) - min(lista[1:])
           
        final.append(valor)
        lista = []
        nova_pilha.push(A[item])
 
    
    lista = []    
    while not nova_pilha.isempty():
            lista.append(nova_pilha.pop())
            
    
            
    if lista[0] == lista[-1]:
           valor = lista[0] - min(lista)
    else:
        valor = max(lista[1:]) - min(lista[1:])
           
    final.append(valor)

    if final == []:
        return 0
    else:
        return max(final) 
    #return lista

#print(solution([4,3,2,2,1]))       
print(solution([3,4,1,4]))
#print(solution([1,3,2,1,2,1,5,3,3,4,2])) 
#print(solution([2,2,2,2,2,2,2,1,2]))       