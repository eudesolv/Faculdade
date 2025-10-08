import pandas as pd
def exportar_csv(pessoas: list, nome_arquivo: str):
    df = pd.dataframe(pessoas)
    df.to_csv(nome_arquivo)