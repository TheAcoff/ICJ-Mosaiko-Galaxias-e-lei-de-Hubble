import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = [3,5,7,8,10,11,22,33]
y = [4,5,2,8,6,9,3,10]

d = {'x': x, 'y': y}

df = pd.DataFrame(data=d)

plt.plot(x,y,'red')
plt.scatter(df['x'],df['y'])
plt.show()