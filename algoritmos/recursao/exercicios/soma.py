def soma(numero):
    resultado = 0
    if numero < 1:
        return resultado
    else:
        resultado += numero
        return resultado + soma(numero - 1)
    
numero = int(input("Informe um número: "))
print(f"A soma dos números de 1 até {numero} é: {soma(numero)}")