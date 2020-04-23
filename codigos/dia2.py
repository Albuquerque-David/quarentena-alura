import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#DESAFIO 1: Rotacionar os thicks (os nomes dos gêneros)
#DESAFIO 2: Comparar outros filmes com notas próximas e achar distribuições bem diferentes
#DESAFIO 3: Pegar 10 filmes com mais votos e fazer boxplot dos 10 filmes um do lado do outro
#DESAFIO 4: Alterar o tamanho do boxplot e com os nomes dos filmes nos thicks (usando o sns)
#DESAFIO 5: Calcular moda, média e mediana de alguns filmes. Explore filmes com notas mais próximas de 0.5, 3 e 5
#DESAFIO 6: Escolher um filme e plotar boxplot e histograma um do lado do outro
#DESAFIO 7: Plotar gráfico das notas médias por ano

avaliacoes = pd.read_csv("../ml-latest-small/ratings.csv")
avaliacoes.columns = ["usuarioId", "filmeId", "nota", "momento"]

filmes = pd.read_csv("../ml-latest-small/movies.csv")
filmes.columns = ["filmeId", "titulo", "generos"]

#RESPOSTA DESAFIO GENEROS
filmes_por_genero = filmes["generos"].str.get_dummies('|').sum().sort_values(ascending=False)

#plt.figure(figsize=(24,8))
#sns.set_style("whitegrid")
#sns.barplot(x=filmes_por_genero.index,
#            y=filmes_por_genero.values,
#            palette=sns.color_palette("BuGn_r",n_colors=len(filmes_por_genero) + 5))
#plt.show()

def plot_filme(n):
    notas_do_filme = avaliacoes.query(f"filmeId=={n}")["nota"]
    print(notas_do_filme.describe())
    notas_do_filme.plot.box()
    plt.show()

#avaliacoesGroup = avaliacoes.groupby("filmeId")
#notas_medias_por_filme = avaliacoesGroup["nota"].mean()
#filmes_com_media = filmes.join(notas_medias_por_filme, on="filmeId")
#filmes_com_media = filmes_com_media.sort_values("nota", ascending=False)
#print(filmes_com_media)

#plot_filme(919)
sns.boxplot(data = avaliacoes.query("filmeId in [1,2,919,46578]"), x="filmeId", y="nota")
plt.show()
