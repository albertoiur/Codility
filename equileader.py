def calcula_dominator(A):
    dados = {}

    for item in A:
        if item not in dados:
            dados[item] = 1
        else:
            dados[item] += 1

    tamanho = len(A) // 2

    for k,v in dados.items():
        if v > tamanho:
            x = k
            
    return x
    
def solution(A):
    pass
        
        
        
                     
print(calcula_dominator([4,3,4,4,2]))