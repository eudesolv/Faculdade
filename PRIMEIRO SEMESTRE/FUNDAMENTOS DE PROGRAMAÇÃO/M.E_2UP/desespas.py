dinheiro_possui = float(input("Digite o valor que possui em sua conta: "))
desespas = float(input("Digite o valor da suas desespas: "))
saldo = dinheiro_possui - desespas
dobro = (dinheiro_possui * 2)
triplo = (dinheiro_possui * 3)

print(f"O saldo disponivel restante é de {saldo:.2f}")
print(f"O saldo que restaria caso recebesse o dobro seria de {dobro - desespas}")
print(f"O saldo que restaria caso recebesse o dobro seria de {triplo - desespas}")
