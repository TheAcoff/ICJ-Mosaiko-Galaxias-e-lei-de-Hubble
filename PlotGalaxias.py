import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot(distmin, distmax):
    df = pd.read_csv('galaxias.csv')
    out = pd.read_csv('outliers.csv')
    #Lei de Hubble
    x = np.linspace(distmin,distmax)
    y = 67.8*x

    #Limpando dados
    df = df.loc[~(df['distance Q unit']<distmin)]
    df = df.loc[~(df['distance Q unit']>distmax)]
    df = df.dropna()

    #Plot de Figuras
    plt.plot(x,y, color="red")
    plt.scatter(df['distance Q unit'],df['radvel'])
    plt.scatter(out['distance Q unit'],out['radvel'], color = 'red')
    plt.xlabel('Distância')
    plt.ylabel('Velocidade Radial')
    plt.title(f'Gráfico - Intervalo {distmin}-{distmax}')
    plt.savefig('Gráfico_Geral.png')
    plt.show()
    

def estatistica(distmax, distmin):
    df = pd.read_csv('galaxias.csv')
    df = df.loc[~((df['distance Q unit']>distmax) | (df['distance Q unit']<distmin))]

    #Cálculos dos dados
    mediana = df['radvel'].median()
    q1, q3 = df['radvel'].quantile([0.25, 0.75])
    upper_limit = q3 + 1.5 * (q3 - q1)
    lower_limit = q1 - 1.5 * (q3 - q1)

    #Arquivo .txt com a estatística:
    with open('boxplot_info.txt', 'w') as arquivo_txt:
        arquivo_txt.write(f"Mediana: {mediana}\n"
            f"Q1: {q1}\n"
            f"Q3: {q3}\n"
            f"Limite Superior: {upper_limit}\n"
            f"Limite Inferior: {lower_limit}\n")
    
    #Tabela dos outliers
    outliers = df.loc[(df['radvel']>upper_limit) | (df['radvel']<lower_limit)]
    outliers = outliers.drop(columns=['#','redshift','cz'])
    outliers.to_csv('outliers.csv', index=False)


def outliers():
    # Ler a tabela .csv
    df = pd.read_csv('galaxias.csv')

    # Separação de 5 em 5
    for i in range(0, 60, 5):
        subset = df.loc[~(df['distance Q unit'] < i) & ~(df['distance Q unit'] > i+5)]  # Subconjunto de 5 linhas
        # Análise usando os quartis
        q1 = subset['radvel'].quantile(0.25)
        q3 = subset['radvel'].quantile(0.75)
        iqr = q3 - q1
        lower_limit = q1 - 1.5 * iqr
        upper_limit = q3 + 1.5 * iqr

        # Filtrar outliers
        outliers = subset.loc[(subset['radvel'] < lower_limit) | (subset['radvel'] > upper_limit)]

        # Gerar novo arquivo .csv com apenas os outliers
        outliers.to_csv(f'outliers_{i}.csv', index=False)

        # Gerar nova tabela .csv sem os outliers
        filtered_df = subset.loc[(subset['radvel'] >= lower_limit) & (subset['radvel'] <= upper_limit)]
        filtered_df.to_csv(f'filtered_df_{i}.csv', index=False)

        #Gráficos
        plt.figure()
        x = np.linspace(i,i+5)
        y = 67.8*x
        plt.plot(x,y, color="red")
        plt.scatter(subset['distance Q unit'], subset['radvel'])
        plt.scatter(outliers['distance Q unit'], outliers['radvel'], color='red')
        plt.xlabel('Distância')
        plt.ylabel('Velocidade Radial')
        plt.title(f'Análise - Intervalo {i}-{i+5}')
        plt.savefig(f'plot_{i}_{i+5}.png')
        plt.close()

        plt.figure()
        plt.boxplot(subset['radvel'])
        plt.title(f'Boxplot - Intervalo {i}-{i+5}')
        plt.savefig(f'boxplot_{i}_{i+5}.png')
        plt.close()


def merge_tables(file_prefix, output_file):
    merged_df = pd.dataFrame()  # dfframe vazio para armazenar os dados mesclados

    for i in range(0, 60, 5):
        file_name = f'{file_prefix}_{i}.csv'
        subset = pd.read_csv(file_name)
        merged_df = pd.concat([merged_df, subset])

    merged_df.to_csv(f'{output_file}.csv', index=False)


def linreg(filename):
    # Ler a tabela .csv
    df = pd.read_csv(filename)

    #definir variáveis
    dist = df['distance Q unit']
    vel = df['radvel']

    #calcular coeficientes
    coeff = np.polyfit(dist, vel, 1)
    reg = np.polyval(coeff, dist)

    print(coeff)

    plt.plot(dist, reg, color='red')
    plt.scatter(dist, vel)
    plt.show()


def coneReg(interv):
    # Ler a tabela .csv
    df = pd.read_csv('galaxias.csv')
    # Separação de 5 em 5
    for i in range(0, 60, interv):
        subset = df.loc[~(df['distance Q unit'] < i) & ~(df['distance Q unit'] > i+interv)]  # Subconjunto de 5 linhas
        # Análise usando os quartis
        q1 = subset['radvel'].quantile(0.25)
        q3 = subset['radvel'].quantile(0.75)
        iqr = q3 - q1
        lower_limit = q1 - 1.5 * iqr
        upper_limit = q3 + 1.5 * iqr

        # Filtrar dados upper e lower
        upper_data = subset.loc[(subset['radvel'] < upper_limit) & (subset['radvel'] > q3)]
        lower_data = subset.loc[(subset['radvel'] > lower_limit) & (subset['radvel'] < q1)]

        #Fazer regressão dos dados upper
        distUpper = upper_data['distance Q unit']
        velUpper = upper_data['radvel']
        coeffUpper = np.polyfit(distUpper, velUpper, 1)
        angUpper, interceptUpper = coeffUpper
        regUpper = np.polyval(coeffUpper, distUpper)

        print(f'{i}-{i+interv}')
        print(coeffUpper)
        plt.scatter(subset['distance Q unit'],subset['radvel'])
        plt.scatter(upper_data['distance Q unit'], upper_data['radvel'], color='red')
        plt.plot(distUpper,regUpper, color='green')
        '''
        distLower = lower_data['distance Q unit']
        velLower = lower_data['radvel']
        '''

'''
distmin = int(input('distmin '))
distmax = int(input('distmax '))
estatistica(distmax, distmin)
merge_tables('outliers', 'outliers_file')
merge_tables('filtered_df', 'filtered')
outliers()
linreg('galaxias.csv')
linreg('filtered.csv')
'''
plot(0,60)

coneReg(4)
