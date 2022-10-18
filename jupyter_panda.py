#Fazendo a importação da biblioteca panda (Usando o Jypter)
import pandas as pd


#Carrega o arquivo para dataframe Pandas
dados = pd.read_csv("data_py\credit.csv")
#Formato
dados.shape

#Resumo estátistica de colunas númericas, porém apenas das colunas númericas
dados.describe()

#Monstra apenas os 5 primeiros registros
dados.head()

#Ultimos registros, com parâmetros, irá pegar os quatro últimos registros
dados.tail(4)

#Filtrando por nome da coluna
dados[["duration"]]

#Filtrando linhas por indice 1 á 3
dados.loc[1:3]

#Trazendo os dados somente das Linhas 1 e 3
dados.loc[[1,3]]

#Filtros - Dentro da minha variável dados ele pegará as informações da coluna chamada purpose e se os dados que esteje dentro dessa coluna (purpose) for igual a radio/tv , ele trazerá as informações
dados.loc[dados["purpose"] == "radio/tv"]






