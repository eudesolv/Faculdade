def duplicados(lista, numero):
    return lista.count(numero) > 1

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

def main():
    for numero in numeros:
        if duplicados(numeros, numero):
            print(f'O número {numero} aparece mais de uma vez na lista.')
        else:
            print(f'O número {numero} aparece apenas uma vez na lista.')

main()
