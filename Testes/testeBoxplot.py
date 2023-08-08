import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(42)
data = np.random.normal(loc=0, scale=1, size=100)
df = pd.DataFrame(data=data, columns=['Numero'])

# Estatísticas descritivas
mediana = df['Numero'].median()
q1, q3 = df['Numero'].quantile([0.25, 0.75])
upper_limit = q3 + 1.5 * (q3 - q1)
lower_limit = q1 - 1.5 * (q3 - q1)

# Boxplot
plt.boxplot(df['Numero'])
plt.title('Boxplot')
plt.xlabel('Variável')
plt.ylabel('Numeroância')


# Salvando informações em um arquivo .txt
with open('boxplot_info.txt', 'w') as arquivo_txt:
    arquivo_txt.write(f"Mediana: {mediana}\n"
            f"Q1: {q1}\n"
            f"Q3: {q3}\n"
            f"Limite Superior: {upper_limit}\n"
            f"Limite Inferior: {lower_limit}\n")

# Criando tabela com outliers
outliers = df.loc[(df['Numero']>upper_limit) | (df['Numero']<lower_limit)]
outliers.to_csv('outliers.csv', index=False)

plt.show()