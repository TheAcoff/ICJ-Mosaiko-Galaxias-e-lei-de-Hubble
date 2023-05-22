import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

tabela = pd.read_csv("Teste 03.csv")
backup = tabela.copy()

tabela = tabela.drop(columns=['typed ident', 'identifier', '#Dist', 'method', 'reference', '#Velo', 'typ','Value    R   m.e.', 'na,Q,dom ','res D'])    