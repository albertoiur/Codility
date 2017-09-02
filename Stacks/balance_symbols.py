# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 15:36:52 2017

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

#Verifica se uma string com 'parenteses' é ou não equilibrada
def balance_simbolos(S):
    #cria uma pilha vazia
    minha_pilha = pilha()
    
    for item in S:
        if item == '(':
            minha_pilha.push(item)
        else:
            if minha_pilha.isempty():
                return False
            else:
                minha_pilha.pop()
                            
    if minha_pilha.isempty():
        return True
    else:
        return False

        
#Verifica se uma string com '([{' é ou não equilibrada

def matches(abrir,fechar):
    abertos = '([{'
    fechados = ')]}'
    
    return abertos.index(abrir) == fechados.index(fechar)
                                
                                
def balance_simbolos_geral(S):
    #Criar uma pilha vazia
    minha_pilha = pilha()
    
    for item in S:
        if item in '([{':
            minha_pilha.push(item)
        else:
            if minha_pilha.isempty():
                return False
            else:
                if matches(minha_pilha.peek(),item):
                    minha_pilha.pop()
                    
    if minha_pilha.isempty():
        return True
    else:
        return False



#Quantos "nested symbols" existem numa string
def how_many_nested(S):
    #Criar uma pilha vazia
    minha_pilha = pilha()
    
    conta = 0
    outra_conta = 0
    #Percorrer toda a string
    for item in S:
        if item=='(':
            minha_pilha.push(item)
            conta += 1
        else:
            if minha_pilha.isempty():
                outra_conta += 1
            else:
                minha_pilha.pop()
                    
    if minha_pilha.isempty():
        return conta
    else:
        outra_conta = outra_conta + len(minha_pilha.mostra_pilha())
        conta -= outra_conta
        return (conta, outra_conta)
    
                        
                            
#Transforma um numero inteiro decimal em binário (usa uma pilha)
def decimal_to_bin(number):
    minha_pilha = pilha()
    s = ''
    while number > 1:
        tmp = number // 2
        resto = number % 2
        number = tmp
        minha_pilha.push(resto)
        
    minha_pilha.push(number) 
    
    while not minha_pilha.isempty():
        s = s + str(minha_pilha.pop())
        
    return s    
        
#Transforma um numero inteiro decimal para qualquer base

def decimal_para_base(number, base):
    digitos = "0123456789ABCDEF"
    s = ''
    minha_pilha = pilha()
    
    while number > 1:
        tmp = number // base
        resto = number % base
        number = tmp
        minha_pilha.push(resto)
    minha_pilha.push(number)
    
    while not minha_pilha.isempty():
        s = s + str(digitos[minha_pilha.pop()])
        
    return s    
        
#def de apoio ao 'calcular_exp_postfixe
def operacao(simbolo, x , y):
    if simbolo == '+':
        return x+y
    if simbolo == '-':
        return x-y 
    if simbolo == '*':
        return x*y
    if simbolo == '/':
        if x >= y:
            return x/y
        else:
            return y/x
        
        
# Calcular o valor de uma expressão Postfix
def calcular_exp_postfixe(S):
    #Criar uma pilha vazia
    minha_pilha = pilha()
    
    #Converter a string S para uma lista    
    lista = S.split(' ')
    
    #Percorrer a lista da esq. para a direita
    for item in lista:
        # Se 'item é um operando converter para inteiro e fazer push na pilha
        if item.isdigit():
            x = int(item)
            minha_pilha.push(x)
        if item in '*/+-':
            op1 = minha_pilha.pop()
            op2 = minha_pilha.pop()
            res = operacao(item,op1,op2)
            minha_pilha.push(res)
    
    return minha_pilha.pop()



A = '7 8 + 3 2 + /'
print(calcular_exp_postfixe(A))




        
        
        
        
        
     
        
        
""" 
A = "(()(())())((("       
print(how_many_nested(A)) 
------------------------------
n = 233
print(decimal_para_base(n,2))
------------------------------  
n = 233
print(decimal_to_bin(n))
------------------------------     
A = "(()(())())"       
print(balance_simbolos(A)) 
--------------------------------
A = '[{()}][]'
print(balance_simbolos_geral(A)) 
"""           