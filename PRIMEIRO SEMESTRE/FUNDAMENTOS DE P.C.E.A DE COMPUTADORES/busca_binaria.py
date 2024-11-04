def busca_binaria(lista, elemento):
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        print(f"Procurando na metade da lista: {lista[esquerda:direita+1]}") 

        if lista[meio] == elemento:
            return meio
        elif lista[meio] < elemento:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1

lista = list(range(101))
elemento = int(input("Digite o elemento a ser buscado: "))
resultado = busca_binaria(lista, elemento)

if resultado != -1:
    print(f"Elemento encontrado na posição {resultado}.")
else:
    print("Elemento não encontrado na lista.")
