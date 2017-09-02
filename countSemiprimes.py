# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 15:53:42 2017

@author: Rui
"""

class deque():
    def __init__(self):
        self.vector = []

    def addFront(self,item):
        self.vector.insert(0,item)
        
    def addRear(self,item):
        self.vector.append(item)
        
    def removeFront(self):
        return self.vector.pop(0)
        
    def removeRear(self):
        return self.vector.pop()
        
    def isempty(self):
        return self.vector == []

    def size(self):
        return len(self.vector)
        
    def mostra_deque(self):
        return self.vector
        
    def criar_fila(self,lista):
        self.vector.extend(lista)
        
def num_primo_v1(n):
    lista = []
    for x in range(2,n):
        isPrime = True
        #print('X = ',x)
        for y in range(2,int(x**0.5)+1):
            #print('Y = ',y)
            if x % y == 0:
                isPrime = False
                break
        if isPrime == True:
            lista.append(x)
    return lista   



        
def solution(N, P, Q):
    fila = deque()
    resultado = list()
    primos = list()
    quadrados = list()
    l1 = []
    conta = 1
    final = []

    intervalos = list(zip(P,Q))
    #Calcular os números primos
    primos = num_primo_v1(N)
    #quadrados dos primos
    for i in primos:
        quadrados.append(i*i)
    
    #criar fila
    fila.criar_fila(primos)
    
    while fila.size() > 1:
        x = fila.removeFront()
        vector = fila.mostra_deque()
        for item in vector:
            resultado.append(x*item)
            
    resultado_tmp = quadrados + resultado
    
    for i in resultado_tmp:
        if i <= N:
            l1.append(i)
    l1.sort()
    
    for item in range(len(intervalos)):
        x = intervalos[item][0]
        y = intervalos[item][1]
        for i in range(x,y):
            if i in l1:
                conta += 1
        final.append(conta)
        conta = 0       
        

        
    
    return final
    

    
    
    
    
    
print(solution(26,[1,4,16],[26,10,20]))        