programa {
  funcao inicio() {
    real distanciaPercorrida, consumoMedio, combustivel

    escreva("Digite a distancia que sera percorrida: ")
    leia(distanciaPercorrida)
    escreva("Digite a quantidade de combustivel: ")
    leia(combustivel)

    consumoMedio = distanciaPercorrida / combustivel
    
    escreva("A m�dia de consumo � de: ", consumoMedio)
  }
}
