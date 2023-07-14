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

df_goodyear = pd.DataFrame(goodyear)
del goodyear

#%%
##### TABLA DE FRECUENCIAS #####

# nro de clases K #

k = np.round(np.emath.logn(2, len(df_goodyear["Price"])), 0)
# la funcion len() retorna el nro de elementos de una secuencia
# np.emath.logn(n,x) nos da el logaritmo de x en base n
# np.round(x,n) redondea un valor x una cantidad n de decimales

i = int(np.ceil(((max(df_goodyear["Price"])-min(df_goodyear["Price"]))/k)/5)*5)
# Limites de clase

lim_s = pd.interval_range(start=125, periods=6, freq=i, closed='left')
lim_i = pd.interval_range(start=335, periods=1, freq=i, closed='both')
# pd.interval_range() retorna un IntervalIndex con los intervalos que queremos
lim = lim_s.append(lim_i)
# .append() agrega otros valores a una lista
df_frequency = pd.DataFrame({
  'Price':lim})

df_frequency['frequency']=df_frequency['Price'].apply(lambda x:df_goodyear[df_goodyear['Price'].between(x.left,
                                                                                                        x.right,
                                                                                                        inclusive=x.closed)]['Price'].size)
df_frequency['relative frequency']=df_frequency['frequency'].apply(lambda x:np.round(x/np.sum(df_frequency['frequency']),3))

# Frecuencias absolutas, frecuencias relativas y frecuencias acumuladas
#"This is a cat: \N{Cat}" From: https://symbl.cc/es/

df_frequency['cumulative frequency']=np.nan
longitud = len(df_goodyear["Price"])
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
    
# Formatear tabla (los cambios solo se mostrarán al exportar la tabla o en jupyter lab) #

df_frequency.style\
  .format(precision=3, thousands=",", decimal=".")\
  .format_index(str.upper, axis=1)

# Diagrama de barras (histograma) de la tabla de frecuencias #

df_frequency.plot.bar(x='Price',
                      y='frequency',
                      rot=0,
                      width=0.9,
                      figsize=(8,6)
                      ).set_title('Histogram \nPrice')

##### HISTOGRAMA PANDAS #####

histograma_pd = df_goodyear["Price"].hist(alpha=0.8, bins=7)

##### HISTOGRAMA PLOTLY#####

histograma = px.bar(df_frequency, x='Price', y='frequency')
#histograma_px = px.histogram(df_goodyear["Price"], x="Price", text_auto=True, nbins=5)
#histograma_px.update_layout(bargap=0.01)
#histograma_px.show()

