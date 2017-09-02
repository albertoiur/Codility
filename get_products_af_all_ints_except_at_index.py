# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 15:01:06 2017

@author: ruialberto
"""

def multiplica_elementos_lista(lista):
    valor = 1
    for i in lista:
        valor = valor * i
    return valor


def get_products_of_all_ints_except_at_index(lista):
    resultado = list()

    if len(lista) < 2:
        raise IndexError('Deve ter pelo menos 2 valores para efectuar multiplicações!')
    copy_lista = lista.copy()

    for num in range(len(lista)):
        copy_lista.pop(num)
        resultado.append(multiplica_elementos_lista(copy_lista))
        copy_lista = lista.copy()

    return resultado

A = [1,2,6,5,9]
#A = [1,0]
print(get_products_of_all_ints_except_at_index(A))
