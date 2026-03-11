
class Node: # Essa classe define a estrutura de um Nó, contendo 
            # o dado armazenado e uma referência para o próximo Nó da lista.
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

def inserirNo(lista, dado): # Com essa função estamos inserindo um novo nó na lista, o tornando o nó atual e nó que já tinha sido inserido se tornando o próximo nó. 
    novoNo = Node(dado)
    novoNo.proximo = lista
    return novoNo


def listarNos(lista): # Essa função lista todos os nós na ordem de pilha,
                      # ou seja, last in first out (LIFO): o último nó inserido é o primeiro exibido.
    atual = lista

    while atual is not None:
        print('-', atual.dado)
        atual = atual.proximo

def removerNo(lista, dado):
    if lista is None:
        print('Lista vazia!!')
        return None
    
    # Está função irá remover um nó da lista, caso o dado do nó seja igual ao dado passado como parâmetro, o nó será removido da lista.
    # Ela irá checar se o nó a ser removido é o primeiro, o nó do meio ou o último nó e irá informar, e caso o nó não esteja na lista será informado também. 

    atual = lista
    anterior = None
    posicao = 0 # linha adicionada para que seja mostrada a posição do Nó removido na lista. 
    
    while atual is not None: 
        if atual.dado == dado:
            if anterior == None:
                print(f'Primeiro nó removido - posição: {posicao}')
                return atual.proximo
            elif atual.proximo == None:
                print(f'Último nó removido - posição: {posicao}')
                anterior.proximo = None
                return lista
            else: 
                print(f'Nó do meio removido - posição: {posicao}')
                anterior.proximo = atual.proximo
                return lista 
        anterior = atual 
        atual = atual.proximo
        posicao += 1

    print('Nó não encontrado!!!')
def buscarNo(lista, dado):
    atual = lista
    posicao = 0 
    while atual is not None: 
        if atual.dado == dado:
            print(f'O Nó foi encontrado - nó: {atual.dado}, posição: {posicao}')
            return True
        atual = atual.proximo
        posicao += 1

    print(f'O Nó com o nó {dado} não foi encontrado!')
    return False




lista = None # Toda lista começa vazia (None), indicando que não há nós.
# Teste de inserção de Nós
lista = inserirNo(None, 1)
lista = inserirNo(lista, 6)
lista = inserirNo(lista, 4)
lista = inserirNo(lista, 3)
lista = inserirNo(lista, 2)
lista = inserirNo(lista, 5)

listarNos(lista)
print('-' * 20)
# Teste de Remoção de Nós 

lista = removerNo(lista, 6)
lista = removerNo(lista, 2)
listarNos(lista)
print('-'* 20)

buscarNo(lista, 4)
buscarNo(lista, 6)
buscarNo(lista, 3)

listarNos(lista)