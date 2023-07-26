# -*- coding: utf-8 -*-
"""
Created on Wed May 24 20:06:01 2023

@author: DELL
"""
#%%
import sys 
sys.path.append("/Docs_python/conexion_sql_datebase")
from conexion_sql_datebase import goodyear
import plotly.io as pio
pio.renderers.default = "browser"
import plotly.express as px
import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

df_goodyear = pd.DataFrame(goodyear)
del goodyear

#%%
##### TABLA DE DISTRIBUCION DE FRECUENCIAS #####

# nro de clases K #

k = np.round(np.emath.logn(2, len(df_goodyear["Price"])), 0)
# la funcion len() retorna el nro de elementos de una secuencia
# np.emath.logn(n,x) nos da el logaritmo de x en base n
# np.round(x,n) redondea un valor x una cantidad n de decimales

n = int(np.ceil(((max(df_goodyear["Price"])-min(df_goodyear["Price"]))/k)/5)*5)
# Limites de clase

lim_s = pd.interval_range(start=125, periods=6, freq=n, closed='left')
lim_i = pd.interval_range(start=335, periods=1, freq=n, closed='both')
# pd.interval_range() retorna un IntervalIndex con los intervalos que queremos
lim = lim_s.append(lim_i)
# .append() agrega otros valores a una lista
df_frequency = pd.DataFrame({
  'Price':lim})

# Frecuencias absolutas, frecuencias relativas y frecuencias acumuladas
#"This is a cat: \N{Cat}" From: https://symbl.cc/es/

df_frequency['frequency']=df_frequency['Price'].apply(lambda x:df_goodyear[df_goodyear['Price'].between(x.left,
                                                                                                        x.right,
                                                                                                        inclusive=x.closed)]['Price'].size)
df_frequency['relative frequency']=df_frequency['frequency'].apply(lambda x:np.round(x/np.sum(df_frequency['frequency']),3))


df_frequency['cumulative frequency']=np.cumsum(df_frequency['frequency'])

"""longitud = len(df_goodyear["Price"])
x = 0
f = []
acum = 0
while x < len(lim):
    for price in df_goodyear["Price"]:
      s = df_frequency.at[x, 'Price']
      if price in s:
        f.append(price)
    # valores de Frecuencias absolutas
    #df_frequency.at[x, 'frequency']=len(f)
    # Valores de Frecuencias relativas
    #df_frequency.at[x, 'relative frequency']=len(f)/longitud
    # Valores de Frecuencias acumulativas
    df_frequency.at[x, 'cumulative frequency']=len(f)+acum
    acum = df_frequency.at[x, 'cumulative frequency']
    x += 1    
    f.clear()

"""    

# Formatear tabla (los cambios solo se mostrarán al exportar la tabla o en jupyter lab) #

df_frequency.style\
  .format(precision=3, thousands=",", decimal=".")\
  .format_index(str.upper, axis=1)
  
### Histograma matplotlib ###

nbins=list(range(lim[0].left, lim.max().right, n))
mdp=df_frequency['Price'].apply(lambda x: x.mid)
fig, ax = plt.subplots()
ax.plot(mdp ,df_frequency['frequency'], marker='o', label=df_frequency['frequency'])
a, bins, figure = ax.hist(df_goodyear['Price'], bins=nbins, edgecolor='black', linewidth=0.5)
ax.set_xlabel("Price")
ax.set_ylabel("Frequency")
ax.set_ylim(0, 35)
ax.set_xlim(120, 340)
for a, mdp in zip(a, mdp):
  ax.text(mdp, a, a, ha='center', va='bottom')

### Diagrama de barras (histograma) de la tabla de frecuencias ###

#fig, ax = plt.subplots()
#ax.bar(df_frequency['Price'].astype('str') ,df_frequency['frequency'])


##### HISTOGRAMA PANDAS #####

histograma_pd = df_goodyear["Price"].hist(alpha=0.8, bins=7)

##### HISTOGRAMA PLOTLY#####

histograma = px.bar(df_frequency, x='Price', y='frequency')
#histograma_px = px.histogram(df_goodyear["Price"], x="Price", text_auto=True, nbins=5)
#histograma_px.update_layout(bargap=0.01)
#histograma_px.show()

