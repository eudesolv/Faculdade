programa {
  funcao inicio() {
    real peso, altura, imc
        
    escreva("Insira sua altura.")
    leia(altura)
    escreva("Insira o seu peso.")
    leia(peso)

    imc = peso / (altura*altura)

    se (imc <= 17 ){
      escreva("Voce est� abaixo do peso")
    }senao se(imc <=18.50 ) {
      escreva("Voce est� no peso normal")
    } senao se(imc <=25){
      escreva("Voce est� acima do peso")
    }senao {
      escreva("Valor de imc n�o registrado")
    }
    

  }
}