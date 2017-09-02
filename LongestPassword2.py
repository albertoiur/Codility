# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 14:23:51 2017

@author: Rui
"""
def Solution(S):
    
    car = 0
    dig = 0
    tmp = []
    maior = 0
    
    palavras = S.split(' ')
    

    valido3 = [p for p in palavras if p.isalnum()] 
    print(valido3)  
    for item in valido3:
        for l in item:
            if l.isdigit():
                dig += 1
            else:
                car += 1
        if car % 2 == 0 and dig % 2!= 0:
            tmp.append(item)
        #if car % 2 == 0 and dig == 0:
            #tmp.append(item)
        if dig % 2 != 0 and car == 0:
            tmp.append(item)
        car = dig = 0    
           
    for i in tmp:
        if len(i) > maior:
            maior = len(i)
    if len(tmp)==0:
        return -1
    
    return maior        
    



S = "test 5 254wexcdolp a0A pass076 ?xy1"
#S = "asdf! 3ab qqqq adw3"
print(Solution(S))