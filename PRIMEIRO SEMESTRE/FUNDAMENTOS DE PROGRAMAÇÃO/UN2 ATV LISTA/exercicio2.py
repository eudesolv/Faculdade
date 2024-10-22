numeros = []

for i  in range(10):
    numero = int(input("Digite um número real: "))
    numeros.append(numero)

print("Os números digitados são: ")
numeros.reverse()
for numero in numeros:
    print(numero)


