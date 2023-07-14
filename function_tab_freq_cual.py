# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 18:40:30 2023

@author: DELL


ReadMe_: Aqui solo se encontrara la funcion y los paquetes a ser importados
"""
#%%
import plotly.io as pio
pio.renderers.default = "browser"
import plotly.express as px
import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt



""" ### CAMBIAR LA EJECUCION DEL CURSOR EN EL ARCHIVO DE CONEXION A LA BASE DE DATOS DE APPLEWOOD A GOODYEAR ### """
import sys 
sys.path.append("/Docs_python/conexion_sql_datebase")
from conexion_sql_datebase import goodyear
df_applewood = pd.DataFrame(goodyear)
del goodyear

#%%

"""## FUNCION QUE RESUELVE TABLA DE DISTRIBUCION DE FRECUENCIAS ABSOLUTAS,
      RELATIVAS Y ACUMULATIVAS DE VARIABLES CUALITATIVAS ## """
      
def tabfreq_cual(dataframe):
  llaves=input('Insert name to group by:')
  df_pre_group = dataframe.groupby(f'{llaves}').size().to_frame(name='count')
  df_group = df_pre_group.assign(relative_count=(lambda x: np.round(x['count'] / np.sum(df_pre_group['count']),3)),
                                 percent_count=(lambda x: x['relative_count'] *100))
  
## Diagrama de barras (Matplotlib)

  fig1, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1)
  
  ax1.bar(x=df_group.axes[0],
          height=df_group['count']
          )
  
  ## Grafica de pastel (Matplotlib)
  
  ax2.pie(df_group['count'],
          labels=df_group.index,
          explode=(0, 0, 0.06, 0))
  ax2.legend(bbox_to_anchor=(1.8, 0.5, 0.2, 0.3),
             title=f'{llaves}')
  
  ## Poligono de frecuencias (matplotlib)
  ax3.plot(df_group.index, df_group['count'])
    
  return df_group


