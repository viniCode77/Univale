def cria_lista():
    # variavel "numeros" vai para a stack 
    # a lista [1, 2, 3] vai para o heap
    numeros = [1, 2, 3]
    return numeros


resultado = cria_lista()
# a função acabou, mas a lista ainda existe no heap
print(resultado) # [1, 2, 3] bb