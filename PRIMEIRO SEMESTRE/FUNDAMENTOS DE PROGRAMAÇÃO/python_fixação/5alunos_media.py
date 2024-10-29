notas_alunos = []

for i in range(5):
    notas = []
    print(f"\nDigite as notas do aluno {i+1}:")
    for j in range(4):
        nota = float(input(f"Digite a nota {j+1}: "))
        notas.append(nota)
    notas_alunos.append(notas)

for i, notas in enumerate(notas_alunos):
    media = sum(notas) / len(notas)
    if media >= 7:
        print(f"Aluno {i+1} aprovado com média {media:.2f}")
    elif 5 <= media < 7:
        print(f"Aluno {i+1} em recuperação com média {media:.2f}")
    else:
        print(f"Aluno {i+1} reprovado com média {media:.2f}")
