import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Ler o arquivo Excel
df = pd.read_excel('data_2019.xlsx')

# Tentar converter a coluna de anos de estudo para números (floats), substituindo valores inválidos por NaN
df[df.columns[1]] = pd.to_numeric(df[df.columns[1]], errors='coerce')

# Remover linhas onde a conversão falhou (ou seja, onde há NaNs)
df = df.dropna(subset=[df.columns[3]])

# Filtrar linhas onde a primeira coluna (territorialidades) não contém 'RM'
df = df[df[df.columns[0]].str.contains('RM', na=False)]

# Ordenar o DataFrame com base na segunda coluna (anos de estudo)
df_sorted = df.sort_values(by=df.columns[1])


# Extrair os dados das colunas após a ordenação
territorialidades = df_sorted.iloc[:, 0]
anos_estudo = df_sorted.iloc[:, 1]
ensino_fundamental = df_sorted.iloc[:, 3]
ensino_medio = df_sorted.iloc[:, 5]
ensino_superior = df_sorted.iloc[:, 6]
renda = df_sorted.iloc[:, 7]

# Criar o gráfico de barras
plt.figure(figsize=(20, 10))
plt.bar(territorialidades, ensino_fundamental, color='blue')
plt.bar(territorialidades, ensino_medio, color='yellow')
plt.bar(territorialidades, ensino_superior, color='orange')

# Adicionar título e rótulos aos eixos
plt.title('Escolaridade (% de conclusão) por Região Metropolitana')
plt.xlabel('Região Metropolitana')
plt.ylabel('Porcentagem')

# Rotacionar os rótulos do eixo X se necessário (para melhor legibilidade)
plt.xticks(rotation=90)

# Exibir o gráfico
plt.tight_layout()
plt.show()
