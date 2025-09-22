from collections import deque

class FilaClinica:
    def __init__(self):
        self.fila = deque()
        self.atendidos = []
    
    def adicionar_paciente(self, nome, prioritario=False):
        """Adiciona paciente à fila"""
        if prioritario:
            self.fila.appendleft(nome) 
            print(f" Paciente PRIORITÁRIO '{nome}' adicionado à fila")
        else:
            self.fila.append(nome)    
            print(f" Paciente '{nome}' adicionado à fila")
    
    def atender_proximo(self):
        if not self.fila:
            print(" Fila vazia - não há pacientes para atender")
            return None
        
        paciente = self.fila.popleft()  # Remove o primeiro da fila
        self.atendidos.append(paciente)
        print(f" Atendendo: {paciente}")
        return paciente
    
    def mostrar_fila(self):
        print(f"\nFila atual ({len(self.fila)} pacientes):")
        if not self.fila:
            print("  (vazia)")
        else:
            for i, paciente in enumerate(self.fila, 1):
                print(f"  {i}. {paciente}")
        print()
    
    def mostrar_atendidos(self):
        print(f"\n PACIENTES ATENDIDOS ({len(self.atendidos)} total):")
        print("=" * 50)
        if not self.atendidos:
            print("  (nenhum paciente foi atendido)")
        else:
            for i, paciente in enumerate(self.atendidos, 1):
                print(f"  {i}º - {paciente}")
        print("=" * 50)


def main():
    clinica = FilaClinica()
    
    print(" SISTEMA DE FILA DA CLÍNICA MÉDICA")
    print("=" * 40)
    
    while True:
        print("\nOpções:")
        print("1. Adicionar paciente normal")
        print("2. Adicionar paciente prioritário")
        print("3. Atender próximo paciente")
        print("4. Ver fila atual")
        print("5. Ver pacientes atendidos")
        print("6. Sair")
        
        opcao = input("\nEscolha uma opção (1-6): ").strip()
        
        if opcao == "1":
            nome = input("Digite o nome do paciente: ").strip()
            if nome:
                clinica.adicionar_paciente(nome, prioritario=False)
            else:
                print("Nome não pode estar vazio!")
        
        elif opcao == "2":
            nome = input("Digite o nome do paciente prioritário: ").strip()
            if nome:
                clinica.adicionar_paciente(nome, prioritario=True)
            else:
                print("Nome não pode estar vazio!")
        
        elif opcao == "3":
            clinica.atender_proximo()
        
        elif opcao == "4":
            clinica.mostrar_fila()
        
        elif opcao == "5":
            clinica.mostrar_atendidos()
        
        elif opcao == "6":
            print("\n Encerrando sistema...")
            clinica.mostrar_atendidos()
            break
        
        else:
            print("Opção inválida! Escolha entre 1 e 6.")


if __name__ == "__main__":
    main()