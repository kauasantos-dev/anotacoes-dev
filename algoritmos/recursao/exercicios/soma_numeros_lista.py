def soma_numeros_lista(lista, indice = 0):
    soma = 0
    if indice == len(lista):
        return 0
    else:
        soma += lista[indice]
        return soma + soma_numeros_lista(lista, indice + 1)

lista_numeros = [10, 10, 10, 10, 10, 10, 10, 10, 10]
print(soma_numeros_lista(lista_numeros))