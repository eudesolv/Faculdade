def é_par(numero):
    return numero % 2 == 0

numero_ingresso = int(input("Digite o número do ingresso: "))

if é_par(numero_ingresso):
    print("Acesso permitido.")
else:
    print("Acesso negado.")
