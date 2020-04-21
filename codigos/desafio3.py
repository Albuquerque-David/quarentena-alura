import pandas as pd
import matplotlib.pyplot as plt

#Desafio 3: Colocar o número de avaliações por filme, isto é, não só a média mas o total de votos

filmes = pd.read_csv("../ml-latest-small/movies.csv")
filmes.columns = ["filmeId", "titulo", "generos"]

avaliacoes = pd.read_csv("../ml-latest-small/ratings.csv")
avaliacoes.columns = ["usuarioId", "filmeId", "nota", "momento"]

avaliacoesGroup = avaliacoes.groupby("filmeId")
numero_votos_filme = avaliacoesGroup["nota"].count()
numero_votos_filme.name = "votos"
notas_medias_por_filme = avaliacoesGroup["nota"].mean()
filmes_com_media = filmes.join(notas_medias_por_filme, on="filmeId")
filmes_com_media_e_votos = filmes_com_media.join(numero_votos_filme, on="filmeId")
print(filmes_com_media_e_votos)

