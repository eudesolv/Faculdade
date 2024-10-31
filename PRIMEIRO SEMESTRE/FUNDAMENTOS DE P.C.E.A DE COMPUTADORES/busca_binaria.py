def busca_binaria(lista, elemento):
    esquerda = 0
    #comprimento da lista / indice final da lista -1 
    direita = len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        # Mostra a parte da lista sendo analisada
        print(f"Procurando na metade da lista: {lista[esquerda:direita+1]}") 

        if lista[meio] == elemento:
            return meio
        elif lista[meio] < elemento:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1

# Exemplo de uso
lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
elemento = int(input("Digite o elemento a ser buscado: "))
resultado = busca_binaria(lista, elemento)

if resultado != -1:
    print(f"Elemento encontrado na posição {resultado}.")
else:
    print("Elemento não encontrado na lista.")
