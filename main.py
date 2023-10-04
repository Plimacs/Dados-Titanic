import pandas as pd
import statistics

# Carrega os arquivos CSV em um DataFrame.
df = pd.read_csv('./Dados/dados4.csv')

# Substitui idades vazias pela moda (valor que aparece com mais frequência) da amostra.
moda_idade = statistics.mode(df['age'])
df['age'].fillna(moda_idade, inplace=True)

# Arredondando as idades para corrigir dados inválidos ou errados.
df['age'] = df['age'].round(0).astype(int)

# Imprime a correção dos dados em "Respostas01.txt"
df.to_csv('./Respostas/Resposta01.txt', index=False)