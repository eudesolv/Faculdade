def media_lista(numeros):
    lista = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

    soma = sum(lista)
    media = soma / len(lista)
    return media

print(media_lista(numeros=[]))
