def soma(numero):
    resultado = 0
    if numero < 1:
        return resultado
    else:
        resultado += numero
        return resultado + soma(numero - 1)

resultado = soma(10)
print(resultado)