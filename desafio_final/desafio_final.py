import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

URI_TREINO = "https://github.com/tgcsantos/quaretenadados/blob/master/DADOS_TREINO.csv?raw=true"
URI_TESTE = "https://github.com/tgcsantos/quaretenadados/raw/master/DADOS_TESTE.csv"
URI_DESAFIOQT = "https://github.com/tgcsantos/quaretenadados/raw/master/DESAFIOQT.csv"

dados_treino = pd.read_csv(URI_TREINO)
dados_teste = pd.read_csv(URI_TESTE)
dados_desafioqt = pd.read_csv(URI_DESAFIOQT)

erro_treino = "Erro ao carregar dados de treino"
erro_teste = "Erro ao carregar dados de teste"
erro_desafioqt = "Erro ao carregar dados de submissão"

assert dados_treino.shape == (150000, 5), erro_treino
assert dados_teste.shape == (20000, 5), erro_teste
assert dados_desafioqt.shape == (10000, 5), erro_desafioqt

# print(dados_desafioqt.describe())
# print(dados_treino.describe())
# print(dados_teste.describe())

# print(dados_treino)
# print(dados_teste)
# print(dados_desafioqt)

coluna_todas = ['NU_NOTA_LC', 'NU_NOTA_CH', 'NU_NOTA_MT', 'NU_NOTA_REDACAO', 'NU_NOTA_CN']
coluna_label = 'NU_NOTA_LC'
coluna_features = ['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']

X_treino = dados_treino[coluna_features].to_numpy()
Y_treino = dados_treino[coluna_label].to_numpy()
X_teste = dados_teste[coluna_features].to_numpy()
Y_teste = dados_teste[coluna_label].to_numpy()
X_desafio = dados_desafioqt[coluna_features].to_numpy()

# corr = dados_treino[coluna_todas].corr()
# ax = plt.subplots(figsize=(11, 8))
# sns.heatmap(corr,  annot=True, annot_kws={"size": 10})
# plt.show()

# x0 = dados_treino['NU_NOTA_CH'].fillna(0)
# x1 = dados_teste['NU_NOTA_CH'].fillna(0)
# sns.distplot(x0)
# sns.distplot(x1)
# plt.legend(labels=['TRAIN', 'TEST'], ncol=2, loc='upper left');
# plt.show()
#
# x0 = dados_treino['NU_NOTA_LC'].fillna(0)
# x1 = dados_teste['NU_NOTA_LC'].fillna(0)
# sns.distplot(x0)
# sns.distplot(x1)
# plt.legend(labels=['TRAIN', 'TEST'], ncol=2, loc='upper left');
# plt.show()
#
# x0 = dados_treino['NU_NOTA_MT'].fillna(0)
# x1 = dados_teste['NU_NOTA_MT'].fillna(0)
# sns.distplot(x0)
# sns.distplot(x1)
# plt.legend(labels=['TRAIN', 'TEST'], ncol=2, loc='upper left');
# plt.show()
#
# x0 = dados_treino['NU_NOTA_REDACAO'].fillna(0)
# x1 = dados_teste['NU_NOTA_REDACAO'].fillna(0)
# sns.distplot(x0)
# sns.distplot(x1)
# plt.legend(labels=['TRAIN', 'TEST'], ncol=2, loc='upper left');
# plt.show()
#
# x0 = dados_treino['NU_NOTA_CN'].fillna(0)
# x1 = dados_teste['NU_NOTA_CN'].fillna(0)
# sns.distplot(x0)
# sns.distplot(x1)
# plt.legend(labels=['TRAIN', 'TEST'], ncol=2, loc='upper left');
# plt.show()

sc = StandardScaler()
y_treino = Y_treino;
x_treino = sc.fit_transform(X_treino)
x_teste = sc.transform(X_teste)
x_desafio = sc.transform(X_desafio)

regressor = RandomForestRegressor(
           criterion='mse',
           max_depth=14,
           warm_start=True,
           n_estimators=300,
)

regressor.fit(x_treino, y_treino)

y_pred_test = regressor.predict(x_teste)
y_pred_test_desafio = regressor.predict(x_desafio)

# print(y_pred_test)
# print(y_pred_test_desafio)

avaliacao_teste = mean_squared_error(Y_teste, y_pred_test)
print("MSE: Teste")
print(avaliacao_teste)

x0 = y_pred_test_desafio
x1 = Y_teste
sns.distplot(x0)
sns.distplot(x1)
plt.legend(labels=['PRED', 'TEST'], ncol=2, loc='upper left');
plt.show()

desafio_df = pd.DataFrame(dados_desafioqt.ID)
desafio_df[coluna_label] = y_pred_test_desafio

desafio_df.to_csv('PREDICAO_DESAFIOQT.csv', index=False)

modelo_dummy = DummyRegressor()
modelo_dummy.fit(X_treino, Y_treino)
dummy_predicoes = modelo_dummy.predict(X_teste)

avaliacao_dummy = mean_squared_error(Y_teste, dummy_predicoes)

print(f"Minha avaliação dummy nos dados de teste foi de {avaliacao_dummy}")
