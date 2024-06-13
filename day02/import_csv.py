#%%

import pandas as pd

df_customer = pd.read_csv ("../data/customers.csv", sep=";")
df_customer

#%%
df_customer.shape

#%% 
df_customer.info(memory_usage="deep")

#%%
df_customer["Points"].describe()

#%%
#Filtering only > 1000 points users
condicao = df_customer["Points"] > 1000

df_customer[condicao]
# %%

#not too common
maximo = df_customer["Points"].max()
condicao = df_customer["Points"] == maximo
df_customer[condicao]

#more common 
condicao = df_customer["Points"] == df_customer["Points"].max()
df_customer[condicao]

#even more common!
df_customer[df_customer["Points"] == df_customer["Points"].max()]

# %%

df_customer[df_customer["Points"] == df_customer["Points"].max()]["Name"].iloc[0]

# %%
condicao = (df_customer["Points"] >= 1000) & (df_customer["Points"] <= 2000)
df_customer[condicao]

# %%
#IMPORTANT!!! make sure to COPY when you want to manipulate the filtered data
condicao = (df_customer["Points"] >= 1000) & (df_customer["Points"] <= 2000)
df_1000_2000 = df_customer[condicao].copy()

df_1000_2000["Points"] = df_1000_2000["Points"] + 1000
df_1000_2000.head()

# %%

df_customer[["UUID", "Name"]]

#%%
columns = df_customer.columns.tolist()
columns.sort()

df_customer = df_customer[columns]
df_customer
#%%

df_customer = df_customer.rename(columns={"Name": "Nome",
                                            "Points": "Pontos"})
df_customer
# %%

df_customer.rename(columns={"UUID": "Id"}, inplace = True)
df_customer
# %%
 