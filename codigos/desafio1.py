import pandas as pd
import matplotlib.pyplot as plt

#Desafio 1: Achar os 18 filmes sem nota

filmes = pd.read_csv("../ml-latest-small/movies.csv")
filmes.columns = ["filmeId", "titulo", "generos"]

avaliacoes = pd.read_csv("../ml-latest-small/ratings.csv")
avaliacoes.columns = ["usuarioId", "filmeId", "nota", "momento"]

avaliacoesGroup = avaliacoes.groupby("filmeId")
notas_medias_por_filme = avaliacoesGroup["nota"].mean()
filmes_com_media = filmes.join(notas_medias_por_filme, on="filmeId")

print(filmes_com_media.query("nota != nota"))



