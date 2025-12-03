package org.example;

import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        UsuarioService service = new UsuarioService();
        int opcao;

        do {
            System.out.println("\n--- MENU CRUD ---");
            System.out.println("1 - Criar usuário");
            System.out.println("2 - Listar usuários");
            System.out.println("3 - Buscar usuário por ID");
            System.out.println("4 - Atualizar usuário");
            System.out.println("5 - Deletar usuário");
            System.out.println("0 - Sair");
            System.out.print("Opção: ");
            opcao = sc.nextInt();
            sc.nextLine();
            switch (opcao) {

                case 1:
                    System.out.print("Nome: ");
                    String nome = sc.nextLine();
                    System.out.print("Email: ");
                    String email = sc.nextLine();
                    Usuario novo = service.criarUsuario(nome, email);
                    System.out.println("Criado: " + novo);
                    break;

                case 2:
                    System.out.println("\n--- Usuários ---");
                    service.listarUsuarios().forEach(System.out::println);
                    break;

                case 3:
                    System.out.print("ID: ");
                    int idBusca = sc.nextInt();
                    Usuario u = service.buscarPorId(idBusca);
                    System.out.println(u != null ? u : "Usuário não encontrado.");
                    break;

                case 4:
                    System.out.print("ID: ");
                    int idAtualizar = sc.nextInt();
                    sc.nextLine();
                    System.out.print("Novo nome: ");
                    String novoNome = sc.nextLine();
                    System.out.print("Novo email: ");
                    String novoEmail = sc.nextLine();
                    if (service.atualizarUsuario(idAtualizar, novoNome, novoEmail)) {
                        System.out.println("Atualizado com sucesso!");
                    } else {
                        System.out.println("Usuário não encontrado.");
                    }
                    break;

                case 5:
                    System.out.print("ID: ");
                    int idDeletar = sc.nextInt();
                    if (service.deletarUsuario(idDeletar)) {
                        System.out.println("Usuário deletado.");
                    } else {
                        System.out.println("Usuário não encontrado.");
                    }
                    break;

                case 0:
                    System.out.println("Saindo...");
                    break;

                default:
                    System.out.println("Opção inválida!");
            }

        } while (opcao != 0);

        sc.close();
    }
}