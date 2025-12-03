package org.example;

import java.util.ArrayList;
import java.util.List;

public class UsuarioService {

    private List<Usuario> usuarios = new ArrayList<>();
    private int proximoId = 1;

    public Usuario criarUsuario(String nome, String email) {
        Usuario usuario = new Usuario(proximoId++, nome, email);
        usuarios.add(usuario);
        return usuario;
    }

    public List<Usuario> listarUsuarios() {
        return usuarios;
    }

    public Usuario buscarPorId(int id) {
        return usuarios.stream()
                .filter(u -> u.getId() == id)
                .findFirst()
                .orElse(null);
    }

    public boolean atualizarUsuario(int id, String nome, String email) {
        Usuario usuario = buscarPorId(id);
        if (usuario != null) {
            usuario.setNome(nome);
            usuario.setEmail(email);
            return true;
        }
        return false;
    }

    public boolean deletarUsuario(int id) {
        return usuarios.removeIf(u -> u.getId() == id);
    }
}