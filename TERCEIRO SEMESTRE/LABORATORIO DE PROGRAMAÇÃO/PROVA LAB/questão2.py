def adicionar_gostos(pessoas: list, gostos: list):
    id_gostos = {}

    for item_gosto in gostos:
        id_gostos[item_gosto["id"]] = item_gosto["gostos"]

    primeiras_5_pessoas = pessoas[:5]

    resultado = []

    for pessoa in primeiras_5_pessoas:
        pessoa_com_gostos = pessoa.copy()
        pessoa_id = pessoa_com_gostos["id"]

        pessoa_com_gostos["gostos"] = id_gostos.get(pessoa_id, [])

        resultado.append(pessoa_com_gostos)

    return resultado

pessoas = []

gostos = []

resultado = adicionar_gostos(pessoas, gostos)

for pessoa in resultado:
    print(pessoa)