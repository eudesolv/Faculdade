def lista_de_compras():
    itens = []
    print("Insira 5 itens para a lista de compras:")

    for i in range(5):
        item = input(f"Item {i+1}: ")
        itens.append(item)

    print("\nSua lista de compras:")
    for item in itens:
        print(item)

    calcular_valor_medio = input("\nDeseja calcular o valor médio de cada item? (s/n): ").lower()

    if calcular_valor_medio == 's':
        valor_total = float(input("Digite o valor total estimado da compra: "))
        valor_medio = valor_total / len(itens)
        print(f"O valor médio de cada item é: R$ {valor_medio:.2f}")
    else:
        print("Cálculo do valor médio não solicitado.")

lista_de_compras()
