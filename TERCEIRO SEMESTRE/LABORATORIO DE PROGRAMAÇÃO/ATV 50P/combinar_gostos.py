def criar_pessoa(nome: str, idade: int, id: int) -> dict:

    return {
        "id": id,
        "nome": nome,
        "idade": idade
    }


def adicionar_gostos(pessoas: list, gostos: list) -> list:

    gostos_dict = {g["id"]: g["gostos"] for g in gostos}
    
    primeiras_cinco = pessoas[:5]
    
    resultado = []
    for pessoa in primeiras_cinco:
        pessoa_com_gostos = pessoa.copy()
        pessoa_com_gostos["gostos"] = gostos_dict.get(pessoa["id"], [])
        resultado.append(pessoa_com_gostos)
    
    return resultado



if __name__ == "__main__":
    pessoas = [
        criar_pessoa("Marcos", 28, 1),
        criar_pessoa("Ana", 24, 2),
        criar_pessoa("Carlos", 30, 3),
        criar_pessoa("Julia", 22, 4),
        criar_pessoa("Pedro", 27, 5),
        criar_pessoa("Laura", 26, 6)
    ]

    gostos = [
        {"id": 1, "gostos": ["Música", "Futebol"]},
        {"id": 2, "gostos": ["Leitura", "Cinema"]},
        {"id": 3, "gostos": ["Viagem"]},
        {"id": 4, "gostos": ["Dança", "Esportes"]},
        {"id": 5, "gostos": ["Tecnologia", "Culinária"]},
        {"id": 6, "gostos": ["Moda"]}
    ]

    resultado = adicionar_gostos(pessoas, gostos)
    

    for pessoa in resultado:
        print(pessoa)