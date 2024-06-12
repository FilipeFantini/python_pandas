#%%
import pandas as pd

#%%

idades = [30, 42, 90, 31]
idades

#%%
media = sum(idades) / len(idades)

total = 0
for i in idades:
    total += (media - i)**2

variancia = total / (len(idades) -1)
variancia
# %%

series_idades = pd.Series(idades)
series_idades
# %%

series_idades.mean()
# %%
series_idades.var()
series_idades.std()

# %%

series_idades.describe()
# %%
series_idades.shape
# %%
