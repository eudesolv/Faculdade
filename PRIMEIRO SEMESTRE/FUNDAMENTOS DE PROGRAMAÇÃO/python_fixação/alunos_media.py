notas = []

for i in range(4):
    nota = float(input("Digite o valor da nota: "))  
    notas.append(nota)

# media é o somatorio de notas divido pelo indice de entradas
media = sum(notas) / len(notas)

if media >= 7:  
    print(f"aluno aprovado com {media}")
elif media >= 5 <= 6.9:
    print(f"aluno em recuperação com {media}")
else:
    print(f"Você está reprovado")