# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 15:48:03 2017

@author: Rui

A palindrome is a string that reads the same forward and backward, for example, radar, toot, and madam. We would like to 
construct an algorithm to input a string of characters and check whether it is a palindrome.
The solution to this problem will use a deque to store the characters of the string. We will process the string from left
 to right and add each character to the rear of the deque. At this point, the deque will be acting very much like an 
 ordinary queue. However, we can now make use of the dual functionality of the deque. The front of the deque will hold the
 first character of the string and the rear of the deque will hold the last character 
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
        
        
def palindro(lista):
    #Criar uma deque
    minha_lista = deque()
    
    for item in lista:
        minha_lista.addRear(item)
        
    tamanho = minha_lista.size()    
    
    while  tamanho > 1:
        frente = minha_lista.removeFront()
        fim = minha_lista.removeRear()
        if frente != fim:
            return False
        tamanho -= 2
        
    return True    
            
#print(palindro("lsdkjfskf"))
#print(palindro("radar"))
print(palindro("madam"))  
#print(palindro('ab'))      