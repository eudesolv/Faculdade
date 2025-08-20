from manager import GerenciadorPessoas

def menu():
    print("\n=== Sistema de Gerenciamento de Pessoas (Sis) ===")
    print("1 - Adicionar pessoa")
    print("2 - Editar pessoa")
    print("3 - Excluir pessoa")
    print("4 - Listar pessoas")
    print("0 - Sair")
    return input("Escolha uma opção: ")

def main():
    gerenciador = GerenciadorPessoas()

    while True:
        opcao = menu()

        if opcao == "1":
            nome = input("Digite o nome: ")
            idade = int(input("Digite a idade: "))
            gerenciador.adicionar_pessoa(nome, idade)

        elif opcao == "2":
            print(gerenciador.listar_pessoas())
            indice = int(input("Digite o índice da pessoa a editar: "))
            novo_nome = input("Novo nome (ou Enter para manter): ")
            nova_idade = input("Nova idade (ou Enter para manter): ")

            gerenciador.editar_pessoa(
                indice,
                novo_nome if novo_nome else None,
                int(nova_idade) if nova_idade else None
            )

        elif opcao == "3":
            print(gerenciador.listar_pessoas())
            indice = int(input("Digite o índice da pessoa a excluir: "))
            gerenciador.excluir_pessoa(indice)

        elif opcao == "4":
            print("\n--- Lista de Pessoas ---")
            print(gerenciador.listar_pessoas())

        elif opcao == "0":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
