pontos = int(input("Digite a quantidade de pontos: "))

if pontos < 1000:
    print("Você é iniciante")
elif 1000 <= pontos < 5000:
    print("Você está na fase intermediária")
else:
    print("Você está na fase avançada")
