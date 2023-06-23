import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

def plot(distmin,distmax):
    df = pd.read_csv('galaxias.csv')
    #Lei de Hubble
    x = np.linspace(distmin,distmax)
    y = 67.8*x

    df = df.loc[~(df['distance Q unit']<distmin)]
    df = df.loc[~(df['distance Q unit']>distmax)]
    df = df.dropna()

    plt.figure(1)
    plt.plot(x,y, color="red")
    plt.scatter(df['distance Q unit'],df['radvel'])
    plt.figure(2)
    plt.boxplot(df['radvel'])
    plt.show()

distmin = int(input('distmin '))
distmax = int(input('distmax '))

plot(distmin,distmax)

'''#Filtro de galaxias
fora = df.loc[df['radvel']>6000]
fora.to_csv('Galaxiasfora25to30.csv')'''