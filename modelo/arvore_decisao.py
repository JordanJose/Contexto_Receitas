import pandas as pd
import numpy

from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

seed = 10

df_registros = pd.read_csv('/mnt/c/Users/jorda/Documents/fabio_ultimo_periodo/pyweb_codigo/bases/registros_usuarios.csv', sep=';')

dic_geral = {}
for coluna in df_registros.columns:
    dic_geral[coluna] = {texto: i for i, texto in enumerate(pd.unique(df_registros[coluna].values))}

dic_pesquisa = {i: texto for i, texto in enumerate(pd.unique(df_registros['pesquisa'].values))}

for coluna in df_registros.columns:
    df_registros[coluna] = df_registros[coluna].replace(dic_geral[coluna])

print(dic_geral)

y = df_registros['pesquisa'].values

X = df_registros.drop('pesquisa', axis=1).values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=seed)

tree = DecisionTreeClassifier(criterion='gini',
                                min_samples_leaf=5,
                                min_samples_split=5,
                                max_depth=None,
                                random_state=seed)

tree.fit(X_train, y_train)

def get_accuracy():
    y_pred = tree.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print('DecisionTreeClassifier accuracy score: {}'.format(accuracy))

def converte_entrada(lista_registro):
    i = 0
    lista_convertida = []
    for coluna in df_registros.columns:
        convertido = dic_geral[coluna][lista_registro[i]]
        lista_convertida.append(convertido)
        i += 1
        if(i+1 == len(df_registros.columns)):
           return lista_convertida

def predicao(lista_registro):
    lista_convertida = converte_entrada(lista_registro)
    resultado = tree.predict([lista_convertida])
    return dic_pesquisa[resultado[0]]