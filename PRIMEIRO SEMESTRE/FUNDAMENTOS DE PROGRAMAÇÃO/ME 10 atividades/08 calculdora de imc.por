programa {
  funcao inicio() {
    real peso, altura, imc
        
    escreva("Insira sua altura.")
    leia(altura)
    escreva("Insira o seu peso.")
    leia(peso)

    imc = peso / (altura*altura)

    se (imc <= 17 ){
      escreva("Voce está abaixo do peso")
    }senao se(imc <=18.50 ) {
      escreva("Voce está no peso normal")
    } senao se(imc <=25){
      escreva("Voce está acima do peso")
    }senao {
      escreva("Valor de imc não registrado")
    }
    

  }
}