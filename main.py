import pandas as pd
import statistics

# Carrega os arquivos CSV em um DataFrame.
df = pd.read_csv('./Dados/dados4.csv')

# Substitui idades vazias ou inválidas pela moda (valor que aparece com mais frequência) da amostra.
moda_idade = statistics.mode(df['age'])
df['age'].fillna(moda_idade, inplace=True)

# Informa a moda de idades.
print('A moda de idades é:', moda_idade)

# Arredondando as idades para corrigir dados inválidos ou errados.
df['age'] = df['age'].round(0).astype(int)

# Imprime a correção dos dados em formato TXT.
df.to_csv('./Respostas/Resposta01.txt', index=False)

Quantidade_Homens = df['sex'].value_counts()['male']
Quantidade_Mulheres = df['sex'].value_counts()['female']

print('Existem', Quantidade_Homens, 'Homens e', Quantidade_Mulheres, 'Mulheres, somando um Total de', Quantidade_Homens + Quantidade_Mulheres, 'pessoas.')

