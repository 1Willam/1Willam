# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 22:13:43 2023

@author: DELL
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
## Tabla de distribucion de frecuencias y frecuencias relativas

df_pre_group = df_applewood.groupby("Location").size().to_frame(name='count')
df_group = df_pre_group.assign(relative_count=(lambda x: np.round(x['count'] / np.sum(df_pre_group['count']),3)),
                               percent_count=(lambda x: x['relative_count'] *100))

#%% 

## Diagrama de barras (Matplotlib)

fig1, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
fig2, ax3 = plt.subplots()

ax1.bar(x=df_group.axes[0],
        height=df_group['count']
        )

## Grafica de pastel (Matplotlib)

ax2.pie(df_group['count'],
        labels=df_group.index,
        explode=(0, 0, 0.06, 0))

ax2.legend(bbox_to_anchor=(1.8, 0.5, 0.2, 0.3),
           title='Locations')

ax3.pie(df_group['count'],
        labels=df_group.index,
        autopct='%1.1f%%',
        pctdistance=1.2,
        labeldistance=.6,
        hatch=['**O', 'oO', 'O.O', '.||.'])

ax3.legend(bbox_to_anchor=(-0.5, 0.3, 0.5, 0.7),
           title='Location')

#%%

## Diagrama de barras (Plotly)

diag_barras=px.bar(df_group,
                   y='count',
                   text_auto=True,
                   pattern_shape=df_group.index,
                   pattern_shape_sequence=[".", "x", "+"])
diag_barras.update_traces(textfont_size=15, textposition="outside")
diag_barras.update_layout(title_text='Tabla de frecuencias (Cualitativas)')
diag_barras.update_traces(marker_color='rgb(158,202,225)',
                          marker_line_color='rgb(8,48,107)',
                          marker_line_width=1.5, opacity=0.6)


## Grafica de pastel (Plotly)

diag_pastel=px.pie(df_group, values='count', names=df_group.index, title='Diagrama de Pastel')
diag_pastel.update_traces(textposition='inside',
                          textinfo='percent+label',
                          textfont_size=20,
                          marker=dict(colors=['gold', 'mediumturquoise', 'darkorange', 'lightgreen'], 
                                     line=dict(color='#000000', width=2)))
