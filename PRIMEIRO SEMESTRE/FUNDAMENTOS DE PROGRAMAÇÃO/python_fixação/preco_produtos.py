
preco = int(input("Digite o valor do produto desejado: "))

if preco <= 100:
    print("Esté produto é considerado barato")
elif preco >= 100 <= 500:
    print("Esté produto tem o preço considerado moderado")
else:
    print("Esté produto tem o preço considerado caro")