class MiniNavegador:
    def __init__(self):
        self.historico = [] 
        self.pagina_atual = None
    
    def acessar_pagina(self, url):
        if self.pagina_atual:
            self.historico.append(self.pagina_atual)
        
        self.pagina_atual = url
        print(f" Acessando: {url}")
    
    def voltar(self):
        """Volta para a página anterior (remove do topo da pilha)"""
        if not self.historico:
            print("Não há páginas anteriores no histórico!")
            return None
        
        print(f"  Saindo de: {self.pagina_atual}")
        self.pagina_atual = self.historico.pop()
        print(f" Voltando para: {self.pagina_atual}")
        return self.pagina_atual
    
    def mostrar_pagina_atual(self):
        """Mostra qual página está sendo exibida atualmente"""
        if self.pagina_atual:
            print(f"Página atual: {self.pagina_atual}")
        else:
            print("Nenhuma página carregada")
    
    def mostrar_historico(self):
        """Mostra todo o histórico de navegação"""
        print(f"\n HISTÓRICO DE NAVEGAÇÃO")
        print("=" * 40)
        
        if not self.pagina_atual and not self.historico:
            print("(nenhuma página visitada)")
        else:
            if self.pagina_atual:
                print(f" ATUAL: {self.pagina_atual}")
            
            if self.historico:
                print("Histórico:")
                for i, pagina in enumerate(reversed(self.historico), 1):
                    print(f"{i}. {pagina}")
            else:
                print("Histórico: (vazio)")
        
        print("=" * 40 + "\n")


def main():
    navegador = MiniNavegador()
    
    print("MINI NAVEGADOR")
    print("=" * 35)
    
    while True:
        print("\nOpções:")
        print("1. Acessar nova página")
        print("2. Voltar página anterior")
        print("3. Ver página atual")
        print("4. Ver histórico completo")
        print("5. Sair")
        
        opcao = input("\nEscolha uma opção (1-5): ").strip()
        
        if opcao == "1":
            url = input("Digite a URL da página: ").strip()
            if url:
                navegador.acessar_pagina(url)
            else:
                print(" URL não pode estar vazia!")
        
        elif opcao == "2":
            navegador.voltar()
        
        elif opcao == "3":
            navegador.mostrar_pagina_atual()
        
        elif opcao == "4":
            navegador.mostrar_historico()
        
        elif opcao == "5":
            print("\n Fechando navegador...")
            navegador.mostrar_historico()
            break
        
        else:
            print("Opção inválida! Escolha entre 1 e 5.")


if __name__ == "__main__":
    main()