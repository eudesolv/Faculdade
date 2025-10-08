def top_tres_maiores(lista):
    top = []
    for i in range(0,3):
        x = max(lista)
        top.append(x)
        lista.remove(x)
    return top

lista = [5, 42, 12, 9, 73, 51, 22]
resultado = top_tres_maiores(lista)
print(resultado)