#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
#%%
data = pd.read_csv('table_03-01.csv')
print(data.columns)
#%%
data['item'].plot(
    xlabel='mes'
)
plt.xticks(
    ticks=range(12), 
    labels=data['mes'],
    rotation=45)
plt.show()
#%%
print(sm.tsa.acf(data['item'], nlags=2))