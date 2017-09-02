# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 18:46:02 2017

@author: Rui

You would like to set a password for a bank account. However, there are three restrictions on the format of the password:

        it has to contain only alphanumerical characters (a−z, A−Z, 0−9);
        there should be an even number of letters;
        there should be an odd number of digits.

You are given a string S consisting of N characters. String S can be divided into words by splitting it at, and removing, the spaces. 
The goal is to choose the longest word that is a valid password. You can assume that if there are K spaces in string S then there are 
exactly K + 1 words.

For example, given "test 5 a0A pass007 ?xy1", there are five words and three of them are valid passwords: "5", "a0A" and "pass007". 
Thus the longest password is "pass007" and its length is 7. Note that neither "test" nor "?xy1" is a valid password, because "?" is not
 an alphanumerical character and "test" contains an even number of digits (zero).
"""
def letras(word):
    conta = 0
    for w in word:
        if w.isalpha():
            conta += 1
    return conta   

def digitos(word):
    conta = 0
    for w in word:
        if w.isdigit():
            conta += 1
    return conta        

def solution(S):
    
    #Guarda cada uma das palavras numa lista
    if len(S)==0:
        return -1
    if len(S)==1:
        if S.isdigit():
            return 1
        else:
            return -1
            
    palavras = S.split()
    maximo = 0
    palavras[:] = [p for p in palavras if p.isalnum()]
    palavras[:] = [p  for p in palavras if letras(p) % 2 == 0]
    palavras[:] = [p for p in palavras if digitos(p) % 2 != 0 or digitos(p) !=0 or letras(p) % 2 == 0]
    
    
    if palavras == []:
        return -1
        
    for w in palavras:
        if len(w) > maximo:
            maximo = len(w)
    
    return (palavras, maximo)
    #return maximo
    
    
S = '4adf4dsk45'
print(solution(S))    