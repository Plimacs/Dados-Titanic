import pandas as pd
import statistics
import matplotlib.pyplot as plt

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
f = open('./Respostas/Resposta01.txt', 'a')
f.write(df.to_string())
f.close()

# Contando todos os Homens e Mulheres da coluna Sex.
Quantidade_Homens = df['sex'].value_counts()['male']
Quantidade_Mulheres = df['sex'].value_counts()['female']

# Informa a quantidade de cada sexo e o total de pessoas.
print('Existem', Quantidade_Homens, 'Homens e', Quantidade_Mulheres, 'Mulheres, somando um total de', Quantidade_Homens + Quantidade_Mulheres, 'pessoas.')

# Conta o número de sobreviventes e não sobreviventes.
contagem_sobreviventes = df['survived'].value_counts()

# Determina os parâmetro da pizza: texto, tamanho, cores, a forma que as fatias 
# são exibidas, sombras, e o ângulo.
labels = ['Não sobreviventes', 'sobreviventes']
sizes = [contagem_sobreviventes[0], contagem_sobreviventes[1]]
colors = ['red', 'green']
explode = (0.1, 0)
autopct = '%1.1f%%'
shadow = True
startangle = 50

# Cria um gráfico de pizza.
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct=autopct, shadow=shadow, startangle=startangle)
plt.axis('equal')

# Exibe o gráfico de pizza.
plt.title('Porcentagem de sobreviventes e não sobreviventes')
plt.show()

# Cria um gráfico de dispersão com dois valores.
plt.scatter(df['age'], df['fare'], alpha=0.5)
plt.xlabel('Idade')
plt.ylabel('Tarifa')

# Exibe o gráfico de Dispersão.
plt.title('Gráfico de Dispersão de Idade vs Tarifa')
plt.show()