# Escrever o passo a passo em portugues
# Traduzir o passo a passo em python
# ------------------------------------
# Passo 1: Importar a base de dados e entender o problema

# Passo 2: Visualizar a base de dados
# - Entnder quais as informaçoes estao disponiveis
# - Descobrir as cagadas da base de dados

# Passo 3: Tratamento de dados
# - Valores que estao reconhecidas de forma errada
# - valores vazios: Valores que nao te ajudam, TE ATRAPALHAM

# Passo 4: Analise inicial
# Passo 5: Analise Mais completa
import plotly.express as px

# Passo 1:
import pandas as pd
tabela = pd.read_csv("telecom_users.csv")

# Passo 2:
# print(tabela)
# churn = cancelamento!!!! (na tabela)
tabela = tabela.drop("Unnamed: 0", axis=1)  # retirei a primeira coluna
# print(tabela)

# Passo 3:
# print(tabela.info())

# Coluna Dtype:
# object = texto / int = numero inteiro/ float = numero com casa decimal

# analisar os valorez vazios = (non-null) de cada coluna
# corrigir isso, por exmeplo, a total gasto

tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# print(tabela.info())
# total gasto = float e 5976 preenchidos. ou seja, eram 10 valorez vazios(comparar com as outras colunas), por ser um valor insinigicante 10 << 5976, entao pode deletar esses casos errados. Se for um numero mt grande, melhor nao deletar

# - valores vazios: Valores que nao te ajudam, TE ATRAPALHAM

# axis = 0 => Deleta linha
# axis = 1 => Deleta coluna

# deletando as colunas vazias
tabela = tabela.dropna(how="all", axis=1)

# deletando as linhas vazias
tabela = tabela.dropna(how="any", axis=0)

# print(tabela.info())

# Passo 4:
# Como estao nossos cancelamentos? 26%?
# churn = cancelamento e vamos calcular a taxa de cancelamento

print(tabela["Churn"].value_counts())
# Isso mostr apra gente no console, os valores de sim e nao de cancelamentos
print("-------------------------")
# em percentual no terminal!!!!
print(tabela["Churn"].value_counts(normalize=True))
print("-------------------------")
print(tabela["Churn"].value_counts(normalize=True).map("{:.2%}".format))

# passo 5:
# Comparar cada coluna da minha tabela com a tabela de cancelamento

# Criar o Grafico

# grafico = px.histogram(tabela, x="Dependentes", color = "Churn") para visualização!!! maneiro

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn")
   # Exibir o grafico
    grafico.show()


#-----------------------------------
# CONLCLUSOES ATRAVES DOS GRAFICOS(storytelling)
# - OLHAR SEMPRE AS COISAS QUE SALTAM OS OLHOS:

# 1 - CLIENTES COM CONTRATO MENSAL TEM MUITO MAIS CHANCES de cancelar
    # - podemos fazer promoçoes para o cliente ir para o contrato anual
# 2 - Familias maiores tendem a cancelar menos do que familias menores
    #- Podemos fazer promoçoes para pessoa pegar uma lista adicional de telefone

# 3 - Meses como clientes maixos tem muito cancelamento. Clientes com pouco tempo como cliente tendem a cancelar muito
    # - A primeira experiencia do cliente na operada, pode estar sendo ruim
    #- Talvez a captação de cliente ta trazendo clientes desqualificados
    #- Ideia: A gente pode criar um incentivo pro cara ficar mais tempo como cliente
# 4 - Quantos mais serviços o cara tem, menos chance dele cancelar
    # -podemos fazer mais promoçoes com mais serviços pro cliente

#5 - Possivel algum problema no serviço de fibra que ta fazendo os clientes cancelarem
    #- Agir sobre a fibra

#6 - Clientes no boleto tem muito mais chance de cancelar, entao temos qeu fazer alguma ação para eles irem para outras formas  de pagamento.