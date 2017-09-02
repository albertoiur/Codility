# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 14:45:53 2017

@author: Rui

We will implement a general simulation of Hot Potato. Our program will input a list of names and a constant, call 
it “num,” to be used for counting. It will return the name of the last person remaining after repetitive counting 
by num. 
To simulate the circle, we will use a queue. Assume that the child holding the potato will be at the front of 
the queue. Upon passing the potato, the simulation will simply dequeue and then immediately enqueue that child, 
putting her at the end of the line. She will then wait until all the others have been at the front before it 
will be her turn again. After num dequeue/enqueue operations, the child at the front will be removed permanently
and another cycle will begin. This process will continue until only one name remains (the size of the queue is 1).
"""

class fila:
    def __init__(self):
        self.vector = []

    def enqueue(self,item):
        self.vector.append(item)
        
    def dequeue(self):
        return self.vector.pop(0)
        
    def isempty(self):
        return self.vector == []

    def size(self):
        return len(self.vector)
        
    def mostrar_fila(self):
        return self.vector
        
        
def hotpot(lista,num):
    #criar uma fila vazia
    minha_fila = fila()
    
    for elem in lista:
        minha_fila.enqueue(elem)
        
    print(minha_fila.mostrar_fila())
    t = minha_fila.size()
    #Enquanto houver mais do que um elemento na Fila
    while  t > 1:
        for count in range(num):
            tmp = minha_fila.dequeue()
            minha_fila.enqueue(tmp)
        minha_fila.vector.pop(0)
        print(minha_fila.mostrar_fila())
        t -= 1
        
    return minha_fila.vector[0]   

lista = ["Bill","David","Susan","Jane","Kent","Brad"]
#lista = ['A', 'B', 'C', 'D', 'E', 'F'] 
print(hotpot(lista,2))
#print(hotpot(lista,2))
        