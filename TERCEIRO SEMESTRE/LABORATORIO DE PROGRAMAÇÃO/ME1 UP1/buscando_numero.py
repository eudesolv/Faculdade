def buscando_numero(lista):
  lista = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

  escolhido = int(input("Digite um número: "))

  if escolhido in lista:
    print(f"O número {escolhido} foi encontrado na lista!")
  else:
    print(f"O número {escolhido} não foi encontrado na lista.")

buscando_numero(lista=[])