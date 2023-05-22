import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#ler o csv e dizer qual o separador
df = pd.read_csv("G06 - 25 a 30.csv", sep=';')

#Tirar as colunas
df = df.drop(columns=['typ','#','#dist','  err-        err+     ',' method ','     reference     '])

#Limpar os espaços (.replace) e fazer eles serem do tipo float (.astype)
df[' distance Q unit'] = df[' distance Q unit'].replace({' ':'', 'Mpc':''}, regex=True).astype(float)

#Limpar os dados maiores ou menores que um valor desejado
df = df.loc[~(df[' distance Q unit']>30)]
df = df.loc[~(df[' distance Q unit']<25)]

#Gerar uma tabela com uma coluna específica
df[' distance Q unit'].to_csv('distance.csv')

#Modo de plot utilizando apenas os pontos
plt.scatter()
plt.plot()