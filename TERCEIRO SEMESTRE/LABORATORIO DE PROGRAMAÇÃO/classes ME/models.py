class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def atualizar_nome(self, novo_nome: str):
        self.nome = novo_nome

    def atualizar_idade(self, nova_idade: int):
        self.idade = nova_idade

    def __str__(self):
        return f"{self.nome} ({self.idade} anos)"
