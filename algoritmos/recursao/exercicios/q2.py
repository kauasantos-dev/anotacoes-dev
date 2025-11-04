def contagem_regressiva(numero):
    if numero < 0:
        return
    else:
        print(numero)
        contagem_regressiva(numero - 1)

contagem_regressiva(10)