def solution(A):

    dados = dict()
    
    for item in A:
        if item not in dados:
            dados[item] = 1
        else:
            dados[item] += 1
    #print('Meu dicionario: ',dados)
    for nome, total in dados.items():
        if total == 1:
            return int(nome)
    
    



    

A = [1000000001,23,23]
x = solution(A)
print ('Elemento unico: ', x)
