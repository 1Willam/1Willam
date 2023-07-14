# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 22:01:06 2023

@author: DELL
"""
#%%
import plotly.io as pio
pio.renderers.default = "browser"
import plotly.express as px
import numpy as np
import pandas as pd
import seaborn as sn


import sys 
sys.path.append("/Docs_python/conexion_sql_datebase")
from conexion_sql_datebase import goodyear
df_goodyear = pd.DataFrame(goodyear)
del goodyear
#%%
"""## FUNCION QUE RESUELVE TABLA DE DISTRIBUCION DE FRECUENCIAS ABSOLUTAS,
      RELATIVAS Y ACUMULATIVAS DE VARIABLES CUANTITATIVAS ## """
    
def tabfreq_cuan(dataframe, column=0, k=0, i=0):
  # Variables
  b = dataframe.axes[1][column]
  label = dataframe[f"{b}"]
  if k==0:
    K = int(np.round(np.emath.logn(2, len(label)), 0))
  else:
    K=k
  if i==0:
    I = int(np.ceil(((max(label)-min(label))/K)/5)*5)
  else:
    I=i
  #I = int(np.ceil((max(label)-min(label))/K))
  #I = int(np.ceil(((max(label)-min(label))/K)/5)*5)
  lim_s = pd.interval_range(start=int(np.floor(min(label))), periods=K-1, freq=I, closed='left')
  lim_i = pd.interval_range(start=(K-1)*I+int(np.floor(min(label))), periods=1, freq=I, closed='both')
  lim = lim_s.append(lim_i)
  x = 0
  f = []
  acum = 0
  # Agregamos columnas al dataframe
  df_frequency = pd.DataFrame({
    f'{b}':lim})
  # Agregamos valores al dataframe
  df_frequency['frequency']=df_frequency[b].apply(
    lambda x:df_goodyear[df_goodyear[b].between(x.left,x.right,inclusive=x.closed)]['Price'].size
    )
  df_frequency['relative frequency']=df_frequency['frequency'].apply(
    lambda x:np.round(x/np.sum(df_frequency['frequency']),3)
    )
    
  while x < len(lim):
    for indice in label:
        s = df_frequency.at[x, f'{b}']
        if indice in s:
          f.append(indice)
      # Valores de Frecuencias acumulativas
    df_frequency.at[x, 'cumulative frequency']=len(f)+acum
    acum = df_frequency.at[x, 'cumulative frequency']
    x += 1    
    f.clear()
  # Histograma PANDAS (diagrama de barras del dataframe)
  df_frequency.plot.bar(x=b,
                        y='frequency',
                        rot=0,
                        width=0.9,
                        figsize=(8,6)
                        ).set_title(f'Histogram \n{b}')
  # Histograma PLOTLY (diagrama de barras del dataframe)
  df_frequency[b]= df_frequency[b].astype('str')
  histograma = px.bar(df_frequency, x=b, y='frequency')
  # Mostrar valores
  print(f"K={K}, \nI={I}, \nlim={lim}, \nmin={min(label)}, max={max(label)}\n{df_frequency}\n{histograma.show()}")
