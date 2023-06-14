import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data = np.random.normal(20,100,100)
df = pd.DataFrame(data=data, columns=['Numero'])

median = df.median()
mean = df.mean()
std = df.std()

print(df)

print (mean,median,std)

plt.boxplot(df)
plt.show()