def media_lista(numeros):
    if not numeros:
        return 0 
    soma = sum(numeros)
    quantidade = len(numeros)
    return soma / quantidade

resultado = media_lista([10, 20, 30, 40])
print(resultado)  # Saída esperada: 25.0
