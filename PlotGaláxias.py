import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Leia a tabela e especifique qual o separador
df = pd.read_csv("C:/Users/ggust/Desktop/Pastas/ICJ/Tabelas/G06 - 25 a 30.csv", sep=';')
distmin = 25
distmax = 30

#Tire os dados indesejados
df  = df.drop(columns=['#','typ','#dist','  err-        err+     ',' method ','     reference     '])

#Limpe os espaços e as unidades de Mpc
df[' distance Q unit'] = df[' distance Q unit'].replace({' ':'', 'Mpc':''}, regex = True).astype(float)
df['   radvel   '] = df['   radvel   '].replace({' ':''}, regex =True).astype(float)

#Eliminar valores menores ou maiores que o intervalo
df = df.loc[~(df[' distance Q unit']<distmin)]
df = df.loc[~(df[' distance Q unit']>distmax)]

#Filtro de galaxias
fora = df.loc[df['   radvel   ']>6000]
fora.to_csv('Galaxiasfora25to30.csv')

#Lei de Hubble
x = np.linspace(distmin,distmax)
y = 67.8*x

#Regressao linear


plt.plot(x,y, color="red")
plt.scatter(df[' distance Q unit'],df['   radvel   '])
plt.savefig('Grafico 25 a 30 Mpc.png')
plt.show()

