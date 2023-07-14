# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 19:46:01 2023

@author: DELL
"""
#%%

import pandas as pd
import numpy as np
import stemgraphic as stm
from stemgraphic import stem_graphic

import sys 
sys.path.append("/Docs_python/conexion_sql_datebase")
from conexion_sql_datebase import goodyear
df_goodyear = pd.DataFrame(goodyear)
del goodyear

#%%

## Media aritmetica Poblacional & Muestral

md=df_goodyear['Price'].mean()

## Mediana

mdn=df_goodyear['Price'].median()

## Moda

mod=df_goodyear['Price'].mode()

## Media geometrica

# med_g = df_goodyear['Percents'].pct_change()

## Rango

rng = df_goodyear['Price'].max()-df_goodyear['Price'].min()

## Varianza Muestral

varm = np.round(df_goodyear['Price'].var(ddof=0),3)

## Varianza Pobalacional
 
varp = np.round(df_goodyear['Price'].var(),3)

## Desviacion Estandar Muestral

stdm=df_goodyear['Price'].std(ddof=0)

## Desviacion Estandar Pobalacional

stdp=df_goodyear['Price'].std()

## Distribución de probabilidad normal

""" ## Cuantiles ## """

## Cuartiles (metodo excel)

cuartil = df_goodyear['Price'].quantile([0.25, 0.5, 0.75])

##  Deciles 

cont = np.arange(0.1, 1, 0.1, dtype=float)
decil = df_goodyear['Price'].quantile(cont)

## Percentil

cont2 = np.arange(0.01, 1, 0.01)
percentil = df_goodyear['Price'].quantile(cont2)

## Sesgo de Pearson (Karl Pearson)

sk = np.round(3*(md-mdn)/stdm,4)

## Sesgo con Minitab y Excel

sk2 = df_goodyear.assign(sesgo=(lambda x: ((x['Price']-md)/stdm)**3))
bias = np.sum(sk2['sesgo'])*(105/(104-103))

## Diagrama de puntos



## Diagrama de tallo y hojas

#fig, ax =stm.stem_graphic(df_goodyear['Distance'])
stm.graphic.stem_graphic(df_goodyear['Size'], df2=df_goodyear['Bath'])
stm.graphic.heatmap(df_goodyear['Bath'],)
stm.graphic.density_plot(df_goodyear['Bath'],)
stm.graphic.stem_graphic(df_goodyear['Distance'], scale=10)
stm.graphic.stem_graphic(df_goodyear['Bath'], scale=1)
