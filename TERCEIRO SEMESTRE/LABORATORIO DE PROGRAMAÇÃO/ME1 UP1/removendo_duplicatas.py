def remeover_duplicatas(numeros):
  for duplicatas in numeros:
    while numeros.count(duplicatas) > 1:
      numeros.remove(duplicatas)

  return numeros

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
numeros = remeover_duplicatas(numeros)
print(numeros)

  