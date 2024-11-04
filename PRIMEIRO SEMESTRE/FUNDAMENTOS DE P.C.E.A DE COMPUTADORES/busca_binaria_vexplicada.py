# função criada para receber uma lista e encontrar o elemento escolhido.
def busca_binaria(lista, elemento):
    esquerda = 0
    #comprimento da lista 
    direita = len(lista) - 1
    # indice final da lista -1 

    # o loop ira continuar enquanto o indice da esquerda for menor que direita
    while esquerda <= direita:
        # calcula o indice do meio da lista atual
        meio = (esquerda + direita) // 2
        # Mostra a parte da lista sendo analisada
        print(f"Procurando na metade da lista: {lista[esquerda:direita+1]}") 

    # Se o elemento do meio for igual ao elemento procurado, retorna o índice do meio.
        if lista[meio] == elemento:
            return meio
        elif lista[meio] < elemento:
            esquerda = meio + 1
        else:
            direita = meio - 1
    # se o elemento do meio for menor que o elemento procurado, ajusta esquerda para meio +1
    # se o elemento meio for maior que o elemento procurado, ajusta direitea para meio -1
    return -1
    # se o loop terminar e o elemtento nao for encontrado retorna -1
    
# Exemplo de uso
lista = list(range(101))
elemento = int(input("Digite o elemento a ser buscado: "))
resultado = busca_binaria(lista, elemento)

if resultado != -1:
    print(f"Elemento encontrado na posição {resultado}.")
else:
    print("Elemento não encontrado na lista.")
