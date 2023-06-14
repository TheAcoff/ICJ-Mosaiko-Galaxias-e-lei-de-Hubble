import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

##Ideias do Bard
# Read the table
df = pd.read_csv('table.csv')

# Get the value column
value = df['dist']
values = value.apply(lambda x: x.split(' '))

# Convert the number column to floats

# Check if the unit is kpc
for value in values:
    if value[1] == 'kpc':
        # Multiply the number by 100
        value[0] = float(value[0]) * 100

for value in values:
    if value[1] in ['kpc', 'Mpc']:
        value[1] = ''
    
df['dist'] = [float(value[0]) for value in values]

# Write the table to a new file
df.to_csv('new_table.csv', index=False)
