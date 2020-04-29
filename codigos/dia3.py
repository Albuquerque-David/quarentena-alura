import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#PERGUNTAS GERAIS
# Aventura tem nota melhor que comédia?
# Diretor com mais filmes tem nota melhor? tem mais faturamento?
# As respostas são específicas para a amostra ou apra o mundo?
# Quais correlações existem entre os dados?
# budget x gross (orçamento x faturamento)
# title_year com algo?

##DESAFIO 1: Boxplot da média do colorido e do preto e branco
##DESAFIO 2: Quem é o que teve o maior prejuízo (próximo de -2.5) e gastou tubos
##DESAFIO 3: Filmes mais recentes tiveram maior prejuízo?
##DESAFIO 4: Quem são os filmes pré 2ª guerra que ganharam tanto
##DESAFIO 5: Confirmar a tese de que o Woody Allen é o ponto no 18 (fez muitos filmes e não faturou)
##DESAFIO 6: Calcular a correlação dos filmes a partir de 2000 e interpretar
##DESAFIO 7: Tentar encontrar uma reta, com excel, python, etc.
##DESAFIO 8:

imdb = pd.read_csv("../movie_metadata.csv")
#print(imdb["color"].value_counts(normalize=True))

color_or_bw = imdb.query("color in ['Color', ' Black and White']")
#print(color_or_bw)

color_or_bw["color_0_ou_1"] = (color_or_bw["color"] == "Color") * 1
#print(color_or_bw["color_0_ou_1"].value_counts())
#sns.scatterplot(data=color_or_bw, x="color_0_ou_1", y="gross")
#plt.show()

#print(color_or_bw.groupby("color").mean()["imdb_score"])

# Lucro / Prejuízo
budget_gross = imdb[["budget", "gross"]].dropna().query("budget > 0 | gross > 0")
#sns.scatterplot(x="budget", y="gross", data=budget_gross)
#plt.show()
#print(imdb.sort_values("budget", ascending=False).head())

imdb = imdb.drop_duplicates()
imdb_usa = imdb.query("country == 'USA'")
#print(imdb_usa.sort_values("budget", ascending=False).head())
budget_gross_usa = imdb_usa[["budget", "gross"]].dropna().query("budget > 0 | gross > 0")
#sns.scatterplot(x="budget", y="gross", data=budget_gross_usa)
#plt.show()

# Relacao com lucro/prejuizo

imdb_usa['lucro'] = imdb_usa['gross'] - imdb_usa['budget']
#sns.scatterplot(x="budget", y="lucro", data=imdb_usa)
#plt.show()

# Lucro / numero filmes do diretor
filmes_por_diretor = imdb_usa["director_name"].value_counts()

imdb_usa['director_name'].value_counts()
gross_director = imdb_usa[["director_name", "gross"]].set_index("director_name").join(filmes_por_diretor, on="director_name")
gross_director.columns = ["money", "filmes_irmaos"]
gross_director = gross_director.reset_index()
#sns.scatterplot(data = gross_director, x="filmes_irmaos", y="money")
#plt.show()

sns.pairplot(data=imdb_usa[["gross", "budget", "lucro", "title_year"]])
plt.show()

print(imdb_usa[["gross", "budget", "lucro", "title_year"]].corr())