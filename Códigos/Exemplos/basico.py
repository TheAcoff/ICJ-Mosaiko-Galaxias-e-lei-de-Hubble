import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

tabela = pd.read_csv('tabelinha.csv')
backup = tabela.copy()

tabela = tabela.drop(columns=['Data','Leitura','Meditação'])

backup.to_csv('backup.csv')
tabela.to_csv('tabelamexida.csv',index=False)

soma = tabela.iloc[1:7,1].sum()