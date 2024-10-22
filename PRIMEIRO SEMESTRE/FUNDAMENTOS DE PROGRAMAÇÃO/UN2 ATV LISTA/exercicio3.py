notas = []

for i  in range(4):
    nota = int(input("Digite sua nota: "))
    notas.append(nota)

    media = sum(notas) / 4

print("Sua média de nota é de: ", media)
