def imprimir_lista(lista, indice = 0):
    if indice == len(lista):
        return
    else:
        print(lista[indice])
        imprimir_lista(lista, indice + 1)

lista_numeros = []
print("Digite dez números:")
for i in range(10):
    lista_numeros.append(input())

print("\nNÚMEROS DA SUA LISTA:")
imprimir_lista(lista_numeros)