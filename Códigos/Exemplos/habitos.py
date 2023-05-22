import matplotlib.pyplot as plt
import pandas as pd

tabela = pd.read_csv('C:/Users/ggust/Desktop/Pastas/Programas/Diversos/tabelinha.csv')
backup = tabela.copy("Backup.csv")

#Deletar coluna
tabela = tabela.drop(columns=['Leitura','Meditação'])

nova = pd.DataFrame(columns=['Semana', 'Soma', 'Media'])

for i in range(16,53):
    if i == 16:    
        j = i-16
        final = j+7
        semana = tabela.iloc[j:final,1].sum()
        media = semana/7
        nova.loc[i] = [i,semana,media]
        final = 7
    else:
        j = final+1
        final = j+7
        semana = tabela.iloc[j:final,1,].sum()
        nova.loc[i] = [i,semana]
        
[linha,coluna]

x = nova['Semana'] 
y = nova['Soma']

plt.bar(x,y)
plt.show()


nova.to_csv('nova.csv', index=False)
tabela.to_csv('tabela.csv')



