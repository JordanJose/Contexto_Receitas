import pandas as pd
from random import randint


receitas = pd.read_csv("receitas_tratadas.csv", sep=';')

def pesquisar_receita(receita):
    regex = r'\b' + receita + r'\b'
    df_filtrado = receitas[receitas['nome'].str.contains(regex, case=False)]
    if(len(df_filtrado) > 5):
        df_filtrado.sample(5, random_state=randint(1, 10), replace=True)
    df_filtrado.reset_index()
    lista_receitas = []
    for index, row in df_filtrado.iterrows():
        lista_receitas.append([row['nome'], str(row['ingredientes']), str(row['modo_de_preparo'])])
    return lista_receitas