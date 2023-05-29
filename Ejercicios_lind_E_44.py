# -*- coding: utf-8 -*-
"""
Created on Thu May 11 22:17:03 2023

@author: DELL
"""

import sys 
sys.path.append("/Docs_python/conexion_sql_datebase")
from conexion_sql_datebase import goodyear
import plotly.io as pio
pio.renderers.default = "browser"
import plotly.express as px
import pandas as pd
import numpy as np

# Creación de DataFrame #

df_goodyear = pd.DataFrame(goodyear)
del goodyear

#### ESTIMACION DE CUARTILES Y VALORES EXTREMOS ####

cuartiles = df_goodyear["Price"].quantile([0, 0.25, 0.5, 0.75, 1])
# ".quantile([])" nos da los cuantiles de una columna sobre 100 que queremos

v_max = cuartiles._get_value(0)
v_min = cuartiles._get_value(1)
q1 = cuartiles._get_value(0.25)
q2 = cuartiles._get_value(0.5)
q3 = cuartiles._get_value(0.75)
# "._get_value()" nos da el valor del indice en una serie

#### ESTIMACION DE VALORES ATIPICOS ####

fs = q3 - q1

v_ap = df_goodyear[(df_goodyear["Price"] < q1 - 1.5*fs)|
                   (df_goodyear["Price"] > q3 + 1.5*fs)][["id", "Price"]]
v_ex = df_goodyear[(df_goodyear["Price"] < q1 - 3 * fs)
                   | (df_goodyear["Price"] > q3 + 3 * fs)][["id", "Price"]]
# df[df.column > exp] nos regresa los valores que la columna cumpla con la expresion

# Rango para valores apartados moderados

r_ap_M = pd.Interval(1.5*fs + q3, 3*fs + q3, closed="both")
r_ap_m = pd.Interval(q1 - 3*fs, q1 - 1.5*fs, closed="both")
# pd.Interval() nos regresa un intervalo de valores que ingresemos

v_md = df_goodyear[(df_goodyear["Price"] == r_ap_M)|
                   (df_goodyear["Price"] == r_ap_m)][["id", "Price"]]

#### DIAGRAMA DE CAJA Y BIGOTE - (PANDAS) ####

pd_cb = df_goodyear.boxplot(
  column="Price",
  fontsize=10,
  rot=45,
  grid=True, 
  showmeans = True,
  figsize=(7, 10),
  whis = 1.5
  ).set_title('Boxplot\nGoodyear-Price')
  
## DIAGRAMA DE CAJA Y BIGOTE - (PLOTLY) ##

pl_cb = px.box(
  df_goodyear["Price"],
  points="all"
  )

pl_cb.show()

## DIAGRAMA DE DISPERSION - (PANDAS) ##

pd_sct = df_goodyear.plot.scatter(
  x='Distance',
  y='Price'
  )

## DIAGRAMA DE DISPERSION - (PLOTLY) ##

pl_sct = px.scatter(
  df_goodyear,
  x="Distance",
  y="Price"
  )
""" Se puede mostrar directamente el grafico con la funcion .show() al final
pl_sct = px.scatter(
  df_goodyear,
  x="Distance",
  y="Price"
  ).show()
"""
pl_sct.show()




