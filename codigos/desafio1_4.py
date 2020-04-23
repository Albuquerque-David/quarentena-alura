import pandas as pd
import matplotlib.pyplot as plt

#Desafio 4: Arredondar os valores para 2 casas decimais

filmes = pd.read_csv("../ml-latest-small/movies.csv")
filmes.columns = ["filmeId", "titulo", "generos"]
filmes = filmes.round(2)
#Printando
#print(filmes)
#DataFrame
#print(filmes.head())

avaliacoes = pd.read_csv("../ml-latest-small/ratings.csv")
#print(avaliacoes.head())
#print(avaliacoes.shape)
#print(len(avaliacoes))

avaliacoes.columns = ["usuarioId", "filmeId", "nota", "momento"]
avaliacoes = avaliacoes.round(2)
#print(avaliacoes.head())
#print(avaliacoes.query("filmeId==1"))
#print(avaliacoes.describe())
#print(avaliacoes["nota"])
#print(avaliacoes.query("filmeId==1").mean())
#print(avaliacoes.query("filmeId==1")["nota"].mean())

avaliacoesGroup = avaliacoes.groupby("filmeId")
#print(avaliacoesGroup)
#print(avaliacoesGroup["nota"].mean())

notas_medias_por_filme = avaliacoesGroup["nota"].mean()
filmes_com_media = filmes.join(notas_medias_por_filme, on="filmeId")
filmes_com_media = filmes_com_media.round(2)
print(filmes_com_media)
#print(filmes_com_media.sort_values("nota"))
#print(filmes_com_media.sort_values("nota", ascending=False))
#print(filmes_com_media.sort_values("nota", ascending=False).head(15))

#avaliacoes.query("filmeId in [2]")["nota"].plot(kind="hist")
#plt.show()