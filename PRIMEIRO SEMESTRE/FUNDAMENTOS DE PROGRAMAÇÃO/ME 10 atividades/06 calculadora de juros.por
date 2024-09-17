programa {
  funcao inicio() {
    real capital, taxa, tempo, juros, montante

    escreva("Digite o valor do capital ")
    leia(capital)
    escreva("Digite o valor da taxa de Juros ")
    leia(taxa)
    escreva("Digite o tempo em meses ")
    leia(tempo)

    taxa = taxa / 100
    juros = capital * taxa * tempo
    montante = capital + juros

    escreva("o valor final é de: ", montante)
  }
}
