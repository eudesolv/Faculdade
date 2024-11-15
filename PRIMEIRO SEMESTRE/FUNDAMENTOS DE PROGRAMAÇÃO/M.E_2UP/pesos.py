def maior_numero(pesos):
    if not pesos:
        return None
    return max(pesos)

pesos_levantados = []
for i in range(1, 6):
    peso = float(input(f"Digite o peso levantado pela pessoa {i}: "))
    pesos_levantados.append(peso)

recorde_atual = maior_numero(pesos_levantados)

if recorde_atual is not None:
    print(f"O recorde atual é: {recorde_atual} kg")
else:
    print("A lista de pesos está vazia.")
