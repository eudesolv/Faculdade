programa {
  funcao inicio() {
    real dinheiro_usuario, cambio_euro_real, cambio_dolar_real, cambio_libra_real
    escreva("Insira o valor desejado em reais. \nR$ ")
    leia(dinheiro_usuario)
    escreva("Insira a taxa de c�mbio do euro para real.\n")
    leia(cambio_euro_real)
    escreva("Insira a taxa de c�mbio do d�lar para real.\n")
    leia(cambio_dolar_real)
    escreva("Insira a taxa de c�mbio da libra para real.\n")
    leia(cambio_libra_real)

    escreva("Valor base: R$ ", dinheiro_usuario, ".\n")
    escreva("Valor em d�lar: ", dinheiro_usuario/cambio_dolar_real, ".\n")
    escreva("Valor em euro: ", dinheiro_usuario/cambio_euro_real, ".\n")
    escreva("Valor em libra: ", dinheiro_usuario/cambio_libra_real, ".\n")
  }
}