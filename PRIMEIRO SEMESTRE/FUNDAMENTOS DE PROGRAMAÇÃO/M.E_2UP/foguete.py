import time

def contagem_regressiva(segundos):
    while segundos > 0:
        print(segundos)
        time.sleep(1)
        segundos -= 1
    print("Lançamento!")

segundos_para_lancamento = int(input("Digite o número de segundos para o lançamento: "))
contagem_regressiva(segundos_para_lancamento)
