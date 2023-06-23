import pandas as pd
import numpy as np

# Carregando as tabelas
tabela1 = pd.read_csv('0a5Mpc.csv')
tabela2 = pd.read_csv('5a10Mpc.csv')
tabela3 = pd.read_csv('10a15Mpc.csv')
tabela4 = pd.read_csv('15a20Mpc.csv')
tabela9 = pd.read_csv('20a25Mpc.csv')
tabela5 = pd.read_csv('25a30Mpc.csv')
tabela6 = pd.read_csv('30a40Mpc.csv')
tabela7 = pd.read_csv('40a50Mpc.csv')
tabela8 = pd.read_csv('50a60Mpc.csv')

# Unindo as tabelas por múltiplas colunas
tabela_unida = pd.concat([tabela1, tabela2,tabela3,tabela4,tabela5,tabela6,tabela7,tabela8,tabela9], axis=0)

# Exibindo a tabela unida
tabela_unida.to_csv('0a60Mpc.csv')
