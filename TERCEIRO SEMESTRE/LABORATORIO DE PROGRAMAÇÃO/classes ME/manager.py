from models import Pessoa

class GerenciadorPessoas:
    def __init__(self):
        self.pessoas = []

    def adicionar_pessoa(self, nome: str, idade: int):
        pessoa = Pessoa(nome, idade)
        self.pessoas.append(pessoa)

    def editar_pessoa(self, indice: int, novo_nome: str = None, nova_idade: int = None):
        if 0 <= indice < len(self.pessoas):
            if novo_nome:
                self.pessoas[indice].atualizar_nome(novo_nome)
            if nova_idade:
                self.pessoas[indice].atualizar_idade(nova_idade)

    def excluir_pessoa(self, indice: int):
        if 0 <= indice < len(self.pessoas):
            self.pessoas.pop(indice)

    def listar_pessoas(self):
        """Retorna lista formatada das pessoas."""
        if not self.pessoas:
            return "Nenhuma pessoa cadastrada."
        
        resultado = "Índice | Nome           | Idade\n"
        resultado += "-" * 30 + "\n"
        for i, pessoa in enumerate(self.pessoas):
            resultado += f"{i:<6} | {pessoa.nome:<14} | {pessoa.idade}\n"
        return resultado
