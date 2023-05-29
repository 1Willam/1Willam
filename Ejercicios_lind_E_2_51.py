# -*- coding: utf-8 -*-
"""
Created on Wed May 24 20:06:01 2023

@author: DELL
"""

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
df_goodyear

##### TABLA DE FRECUENCIAS #####

# nro de clases K #

k = np.round(np.emath.logn(2, len(df_goodyear["Price"])), 0)
# la funcion len() retorna el nro de elementos de una secuencia
# np.emath.logn(n,x) nos da el logaritmo de x en base n
# np.round(x,n) redondea un valor x una cantidad n de decimales

i = np.round((max(df_goodyear["Price"])-min(df_goodyear["Price"]))/k, 1)


## Histograma ##




histograma_px = px.histogram(df_goodyear["Price"], x="Price", text_auto=True, nbins=5)
histograma_px.update_layout(bargap=0.01)
histograma_px.show()

histograma_pd = df_goodyear["Price"].hist(alpha=0.8, bins=5)
