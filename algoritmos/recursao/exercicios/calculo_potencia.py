def potencia(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * potencia(base, expoente - 1)

print("CÁLCULO DE POTÊNCIA\n")
base = int(input("Informe a base: "))
expoente = int(input("Informe o expoente: "))
print(f"{base}^{expoente} = {potencia(base, expoente)}")