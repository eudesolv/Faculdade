def somar_lista(natureza, tecnologia):
    natureza = ["rio", "floresta", "leão", "montanha", "oceano", "estrela", "vento", "cachoeira", "lua", "girassol"]

    tecnologia = ["algoritmo", "API", "blockchain", "código", "software", "nuvem", "hardware", "interface", "pixel", "servidor"]

    lista_soma = natureza + tecnologia

    return lista_soma

print(somar_lista([], []))