import pandas as pd

# Exemplo leitura csv
df = pd.read_csv("C:/Users/Gustavo Rocha Campos/Downloads/CSV_de_dados_aleat_rios__10_colunas_x_50_linhas_.csv")

dtDados = {
    "Nome": ["Gustavo", "Fernanda"],
    "Idade": [36, 27]
}

# Exemplos aleatórios
print(df.head())  # Print das 5 primeiras linhas
print(df.tail())  # Print das 5 últimas linhas
print(df.info())
print(df.describe())

# Exemplos de loc
dfDados = pd.DataFrame(dtDados)
print(dfDados)

dfDados.loc[dfDados["Idade"] > 20, "Idade"] = 20
print(dfDados)

dfDados.loc[0, "Idade"] = 25
print(dfDados)
