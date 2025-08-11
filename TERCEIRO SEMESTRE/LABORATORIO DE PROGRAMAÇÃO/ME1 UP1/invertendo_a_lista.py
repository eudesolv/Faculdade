def inverter_lista(lista):
    numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

    inverter_numeros = []
    for numero in numeros:
        if numero in lista:
            inverter_numeros.append(numero)
    inverter_numeros.reverse()
    return inverter_numeros

lista = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
resultado = inverter_lista(lista)
print(resultado)
