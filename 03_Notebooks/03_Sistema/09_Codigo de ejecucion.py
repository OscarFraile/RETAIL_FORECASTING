#!/usr/bin/env python
# coding: utf-8


# In[1]:


import warnings
warnings.filterwarnings("ignore")

#Cargar las funciones auxiliares
from FuncionesAuxiliares import *

#Cargar los datos
ruta_proyecto = 'C:/Users/Oscar/OneDrive - FM4/Escritorio/Python Data Mastery/EstructuraDirectorio/03_MACHINE_LEARNING/08_CASOS/002_RETAIL'
nombre_fichero_datos = 'DatosParaProduccion.csv'
ruta_completa = ruta_proyecto + '/02_Datos/02_Validacion/' + nombre_fichero_datos
df = pd.read_csv(ruta_completa,sep=';',parse_dates=['date'],index_col='date')

#Seleccionar solo las que se han usado
variables_finales = ['store_id',
                     'item_id',
                     'event_name_1',                     
                     'month',
                     'sell_price',                      
                     'wday',
                     'weekday',
                     'ventas']

df = df[variables_finales]

#Lanzar la predicción
forecast = forecast_recursivo(df).sort_values(by = ['store_id','item_id'])

