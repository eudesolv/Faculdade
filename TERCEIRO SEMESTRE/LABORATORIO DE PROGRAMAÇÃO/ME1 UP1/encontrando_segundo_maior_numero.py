def segundo_maior(lista):
    lista = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

    if lista:
        maior_numero = max(lista)
        lista.remove(maior_numero)
        segundo_maior = max(lista)
        return segundo_maior
    else:
        return None
    
print(segundo_maior([]))