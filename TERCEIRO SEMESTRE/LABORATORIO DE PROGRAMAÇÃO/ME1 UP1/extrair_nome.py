def extrair(lista):
    return list(lista.keys())

dados = {"animal": "gato", "cor": "preto", "idade": 5}
nomes = extrair(dados)
print(nomes)  