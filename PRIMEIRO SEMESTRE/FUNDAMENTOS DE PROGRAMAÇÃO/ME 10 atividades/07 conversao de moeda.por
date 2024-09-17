programa {
  funcao inicio() {
    real reais, dolar, cambio, valorReal, valorCambioDolar

    escreva("Digite o valor em reais: ")
    leia(valorReal)
    escreva("Digite o valor do cambio do dia do dolar: ")
    leia(valorCambioDolar)

    cambio = valorReal * valorCambioDolar

    escreva("esse é o valor do cambio equivalente em dolares: ", cambio)

  }
}
