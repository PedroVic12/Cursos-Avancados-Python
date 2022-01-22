import pandas as pd  # importar base de dados do excel
import seaborn as sns  # Graficos em python
import matplotlib.pyplot as plt  # Graficos em python

# inteligencia artificial(separar em simulação e prova)
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression  # Teste 1 da inteligencia
from sklearn.ensemble import RandomForestRegressor  # Teste 2 da inteligencia

from sklearn.metrics import r2_score  # analise dos testes da IA com porcentagem

import os
os.system("cls")

# =====> Passo a Passo de um Projeto de Ciência de Dados

# - Passo 1: Entendimento do Desafio
# - Passo 2: Entendimento da Área/Empresa
# - Passo 3: Extração/Obtenção de Dados
# - Passo 4: Ajuste de Dados (Tratamento/Limpeza)
# - Passo 5: Análise Exploratória
# - Passo 6: Modelagem + Algoritmos (Aqui que entra a Inteligência Artificial, se necessário)
# - Passo 7: Interpretação de Resultados

tabela = pd.read_csv("advertising.csv")
print(tabela)
# Tabela vendas esta em escalas diferentes(provavelmente em milhoes)
# tabela ja esta com limpeza. (tratamento de dados)

# ------------------------------------
# Passo 5: Analise Exploratoria
# - Vamos tentar visualizar como as informações de cada item estão distribuídas
# - Vamos ver a correlação entre cada um dos itens
# - USando graficos

# # # criar o grafico
# sns.pairplot(tabela)
# # # exibir o grafico
# plt.show()

# # criar o grafico
# sns.heatmap(tabela.corr(), cmap="Wistia", annot=True)
# # exibir o grafico
# plt.show()


# - Passo 6: Marchine learning

# separar os dados em x e y
y = tabela["Vendas"]
x = tabela[["TV", "Radio", "Jornal"]]

# separar os dados em treinos e testes
x_treino, x_teste, y_treino, y_teste = train_test_split(
    x, y, test_size=0.3, random_state=1)
# treina um simulação

# Testar na provar pra ver se aprendeu

# Criar a inteligencia
modelo_regressaoLinear = LinearRegression()
modelo_arvoreDecisao = RandomForestRegressor()
# Treinar a inteligencia
modelo_regressaoLinear.fit(x_treino, y_treino)
modelo_arvoreDecisao.fit(x_treino, y_treino)

# Compara as previsoes com o gabarito em porcentagem
previsao_regressaolienar = modelo_regressaoLinear.predict(x_teste)
previsao_arvoredecisao = modelo_arvoreDecisao.predict(x_teste)
print(r2_score(y_teste, previsao_regressaolienar))
print(r2_score(y_teste, previsao_arvoredecisao))

# o melhor modelo é o de arvore de decisao!!! (96,4%)

# Agora usar esse modelo para fazer novas previsoes
novos_valores = pd.read_csv("novos.csv")
nova_previsao = modelo_arvoreDecisao.predict(novos_valores)
print(novos_valores)
print("--------------------------")
print(nova_previsao)