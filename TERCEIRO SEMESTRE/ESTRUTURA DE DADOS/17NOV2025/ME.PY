class MaxHeap:
  def __init__(self):
    #todo nosso heap inicia vazio
    self.heap= []


  #essa função "pai" retornar o nosso índice do nó "i"
  def pai(self,i):
    return (i -1) //2


  #essa função vai retornar o filho esquerdo do nó "i"
  def filho_esquerdo(self,i):
    return  2* i + 1


  #essa função vai retornar o filho direita do nó "i"
  def filho_direito(self,i):
    return  2* i + 2


  #função trocar posição no HEAP
  def trocar(self,i, j):
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


  #criação da função "subir" "HEAPFY UP"
  def subir(self,i):
    while i > 0 and self.heap[self.pai(i)] < self.heap[i]:
      #trocar o nosso pai
      self.trocar(i, self.pai(i))
      #atualizar a nossa lista
      i = self.pai(i)


  #criação da função "descer" "HEAPFY DOWN"


  def descer(self,i):
    tamanho = len(self.heap)
    maior = i
    esquerda = self.filho_esquerdo(i)
    direito = self.filho_direito(i)


    #verificar se o filho esquerdo existir e se é maior
    if esquerda < tamanho and self.heap[esquerda] > self.heap[maior]:
      maior = esquerda


    #verificar se o filho direita vai existir e se é maior
    if direito < tamanho and self.heap[direito] > self.heap[maior]:
      maior = direito


    #se o maior não o atual, então troca e continua
    if maior != i:
      self.trocar(i, maior)
      self.descer(maior)

   #inserir elementos
  def inserir (self, valor):
    """
    Add elemento da array
    vamos usar heapfy up para manter a prioridade de heap
    """
    print(f"Inserido {valor}")
    self.heap.append(valor)
    self.subir(len(self.heap)-1)
    print(f"Heap após inserção: {self.heap}")


    #extrair o "valor máximo"
  def extrair_maaximo(self):
    """
    Extrair máximo (remove e retorna a raiz(MAIOR ELEMENTO))
    passo 1: move o ultimo elemento da raiz
    passoa 2: aplicar heapfy down para reorganizar.
    """
    if len(self.heap) == 0:
      return None

    if len(self.heap) == 1:
      return self.heap.pop()


    #criar variável para guardar o maximo
    maximo = self.heap[0]


    #mover o ultimo elemento para a nossa raiz
    self.heap[0] = self.heap.pop()


    #reorganizar o heap
    self.descer(0)


    print(f"Extraido maximo: {maximo}")
    print(f"Heap após extração: {self.heap}")

  def visualizar(self):
    print("\n Heap atual: ", self.heap)
    return len(self.heap)

  def tamanho(self):
    return len(self.heap)

  def maior(self):
    if len(self.heap) == 0:
      return None
    return self.heap[0]


  if __name__ == "__main__":
    h = MaxHeap()

    h.inserir(10)
    h.inserir(4)
    h.inserir(15)
    h.inserir(20)

    h.visualizar()

    print("Tamanho do heap ", h.tamanho())
    print("Maior elemento: ", h.maior()) 


    h.extrair_maaximo()

    h.visualizar()
