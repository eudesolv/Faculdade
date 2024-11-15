def inverter_string(mensagem):
    return mensagem[::-1]

mensagem_secreta = input("Digite a mensagem secreta: ")
mensagem_decifrada = inverter_string(mensagem_secreta)
print(f"A mensagem decifrada é: {mensagem_decifrada}")
