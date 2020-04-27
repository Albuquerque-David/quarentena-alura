import pandas as pd
import matplotlib.pyplot as plt

# Desafio 1: Achar os 18 filmes sem nota
# Desafio 2: Mudar o nome da coluna nota para media após o join
# Desafio 3: Colocar o número de avaliações por filme, isto é, não só a média mas o total de votos
# Desafio 4: Arredondar os valores para 2 casas decimais
# Desafio 5: Mostrar quais gêneros de filmes
# Desafio 6: Contar quantos tem de cada gênero
# Desafio 7: Plotar o gráfico de aparições por gênero (tipo = barra)

# Lendo documentos
from pandas.tests.frame.test_sort_values_level_as_str import ascending

filmes = pd.read_csv("../ml-latest-small/movies.csv")
filmes.columns = ["filmeId", "titulo", "generos"]
# Printando
# print(filmes)
# DataFrame
# print(filmes.head())

avaliacoes = pd.read_csv("../ml-latest-small/ratings.csv")
# print(avaliacoes.head())
# print(avaliacoes.shape)
# print(len(avaliacoes))

avaliacoes.columns = ["usuarioId", "filmeId", "nota", "momento"]
# print(avaliacoes.head())
# print(avaliacoes.query("filmeId==1"))
# print(avaliacoes.describe())
# print(avaliacoes["nota"])
# print(avaliacoes.query("filmeId==1").mean())
# print(avaliacoes.query("filmeId==1")["nota"].mean())

avaliacoesGroup = avaliacoes.groupby("filmeId")
# print(avaliacoesGroup)
# print(avaliacoesGroup["nota"].mean())

notas_medias_por_filme = avaliacoesGroup["nota"].mean()
filmes_com_media = filmes.join(notas_medias_por_filme, on="filmeId")
# print(filmes_com_media)
# print(filmes_com_media.sort_values("nota"))
# print(filmes_com_media.sort_values("nota", ascending=False))
# print(filmes_com_media.sort_values("nota", ascending=False).head(15))

avaliacoes.query("filmeId in [2]")["nota"].plot(kind="hist")
plt.show()
