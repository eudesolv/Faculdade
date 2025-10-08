def criar_pessoa(nome: str, idade: int, id: int) -> dict:
    return {
        "id": id,
        "nome": nome,
        "idade": idade
    }

p1 = criar_pessoa("Marcos", 18, 1)
p2 = criar_pessoa("Fernanda", 43, 2)
p3 = criar_pessoa("Gabriela", 55, 3)
    
print(p1)
print(p2)
print(p3)