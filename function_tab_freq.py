# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 22:01:06 2023

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

#%%

def tab_freq(dataframe, column=1):
  # Variables
  b = dataframe.axes[1][column]
  label = dataframe[f"{b}"]
  k = int(np.round(np.emath.logn(2, len(label)), 0))
  i = int(np.ceil((max(label)-min(label))/k))
  #i = int(np.ceil(((max(label)-min(label))/k)/5)*5)
  lim_s = pd.interval_range(start=int(np.floor(min(label))), periods=k-1, freq=i, closed='left')
  lim_i = pd.interval_range(start=(k-1)*i+int(np.floor(min(label))), periods=1, freq=i, closed='both')
  lim = lim_s.append(lim_i)
  longitud = len(label)
  x = 0
  f = []
  acum = 0
  # Agregamos columnas al dataframe
  df_frequency = pd.DataFrame({
    f'{b}':lim,
    'frequency':np.nan,
    'relative frequency':np.nan,
    'cumulative frequency':np.nan
    })
  # Agregamos valores al dataframe
  while x < len(lim):
      for indice in label:
        s = df_frequency.at[x, f'{b}']
        if indice in s:
          f.append(indice)
      # valores de Frecuencias absolutas
      df_frequency.at[x, 'frequency']=len(f)
      # Valores de Frecuencias relativas
      df_frequency.at[x, 'relative frequency']=np.round(len(f)/longitud,2)
      # Valores de Frecuencias acumulativas
      df_frequency.at[x, 'cumulative frequency']=len(f)+acum
      acum = df_frequency.at[x, 'cumulative frequency']
      x += 1    
      f.clear()
  # Histograma (diagrama de barras del dataframe)
  df_frequency.plot.bar(x=f'{b}',
                        y='frequency',
                        rot=0,
                        width=0.9,
                        figsize=(8,6)
                        ).set_title(f'Histogram \n{b}')
  # Mostrar la tabla de fecuencias
  print(f"k={k}, i={i}, lim={lim}, min={min(label)}, max={max(label)}\n", df_frequency)