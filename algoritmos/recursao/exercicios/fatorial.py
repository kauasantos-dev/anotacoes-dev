def fatorial(numero):
    if numero == 1 or numero == 0:
        return 1
    else:
        return numero * fatorial(numero - 1)
    
    # A função não retorna um valor pronto ainda
    # A função retorna uma chamada dela mesma, logo, será executada novamente
    # A cada nova chamada, vai empilhando uma execução sobre a outra
    # Quando o número atinge o seu caso base, as chamadas começam a desimpilhar, sendo resolvidas uma por uma

resultado = fatorial(5)
print(resultado)