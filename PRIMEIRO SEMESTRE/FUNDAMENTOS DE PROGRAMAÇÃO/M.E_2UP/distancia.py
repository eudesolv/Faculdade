def monitorar_progresso(distancia):
    for km in range(1, distancia + 1):
        print(f"Você percorreu {km} km.")
        print(f"Faltam {distancia - km} km para o fim da meta.")
        print("-----------")

distancia = int(input("Digite a distância que deseja percorrer (em km): "))
monitorar_progresso(distancia)
