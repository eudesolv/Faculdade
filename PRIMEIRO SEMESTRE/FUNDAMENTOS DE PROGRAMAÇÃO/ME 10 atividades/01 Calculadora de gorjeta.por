programa {
  funcao inicio() {
    real valorConta, gorjeta, valorTotal

    escreva("Digite o valor da sua conta: ")
    leia(valorConta)

    gorjeta = valorConta * 0.10
    valorTotal = gorjeta + valorConta

    escreva("O valor final da sua conta é de: ", valorTotal)
  }
}
