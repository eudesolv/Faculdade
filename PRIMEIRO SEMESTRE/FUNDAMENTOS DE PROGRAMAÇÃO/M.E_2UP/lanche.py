def soma(valor1, valor2):
    return valor1 + valor2

valor_pessoa1 = float(input("Digite o valor dos itens do lanche da primeira pessoa: "))
valor_pessoa2 = float(input("Digite o valor dos itens do lanche da segunda pessoa: "))

total = soma(valor_pessoa1, valor_pessoa2)

print(f"O valor total que deverá ser pago é: R$ {total:.2f}")
