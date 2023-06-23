import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def format(distmin, distmax):
    def convert(col):
        df[col] = df[col].replace({' ':'', 'Mpc':' Mpc', 'kpc':' kpc',}, regex = True).astype(str)
        value = df[col] 
        values = value.apply(lambda x: x.split(' '))

        for value in values:
            if value[1] == ' kpc':
                value[0] = float(value[0]) * 0.001

            df[col] = [float(value[0]) for value in values]
            return df[col]
    
    def limp(col):
        df[col] = df[col].replace({' ':''}, regex = True).astype(float)
        return df[col]
    
    #Leia a tabela e especifique qual o separador
    df = pd.read_csv("C:/Users/ggust/Desktop/Pastas/ICJ/Tabelasnform/{}a{}.csv".format(distmin,distmax), sep=';')

    #Tire os dados indesejados
    df  = df.drop(columns=['typ','#dist','err-err+','method','reference'])

    #Limpe os espaços e as unidades de Mpc, e converte os dados
    df['distance Q unit'] = convert('distance Q unit')
    df['radvel'] = limp('radvel')

    #Eliminar valores menores ou maiores que o intervalo
    df = df.loc[~(df['distance Q unit']<distmin)]
    df = df.loc[~(df['distance Q unit']>distmax)]
    df = df.dropna()

    #Nova Tabela
    df.to_csv('{}a{}Mpc.csv'.format(distmin, distmax),index=False)

for i in range(0,30,5):
   format(i,i+5)

for i in range(30,60,10):
    print(i)
    format(i,i+10)