import pandas as pd
import matplotlib.pyplot as plt

#Desafio 5: Mostrar quais gêneros de filmes
#Desafio 6: Contar quantos tem de cada gênero
#Desafio 7: Plotar o gráfico de aparições por gênero (tipo = barra)

# Lendo documentos
from pandas.tests.frame.test_sort_values_level_as_str import ascending

filmes = pd.read_csv("../ml-latest-small/movies.csv")
filmes.columns = ["filmeId", "titulo", "generos"]
generos = []

text = filmes.groupby("generos").count()
text = filmes["generos"].str.split("|")
for x in text:
    for y in x:
        generos.append(y)

print(generos)
filmes = pd.DataFrame({'generos':generos})
filmes_por_genero = filmes.groupby("generos")["generos"].count()
print(filmes_por_genero)
filmes_por_genero.plot(kind="bar")
plt.show()



