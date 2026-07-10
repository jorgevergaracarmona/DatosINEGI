#!/usr/bin/env python
# coding: utf-8

# In[8]:


# cargamos dataframes de trabajo.
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
#import snowflake.connector
#import streamlit_option_menu
#from streamlit_option_menu import option_menu

CARPETA_RAIZ = Path(__file__).resolve().parents[1]

DIRECTORIO = CARPETA_RAIZ / "Datos" / "Datos" / "ModeloDatos" 

CATALOGOS = DIRECTORIO / "catalogos"
DICCIONARIO = DIRECTORIO / "diccionario_de_datos"
CONJUNTO_DATOS = DIRECTORIO / "conjunto_de_datos"

@st.cache_data
#def carga_df():
#Carga la informacion en dataframes para la app."""

df_cat_entidades = pd.read_csv(CATALOGOS / "cve_ent.csv")
df_cat_tam_pob = pd.read_csv(CATALOGOS / "menor10.csv")
df_cat_respuesta = pd.read_csv(CATALOGOS / "p2_4_01.csv")
df_cat_respuesta_1 = pd.read_csv(CATALOGOS / "p3_14_1.csv")
    
df_cat_preguntas = pd.read_csv(DICCIONARIO / "diccionario_datos_enut_2024_thogar.csv")

df_tabla_hogar = pd.read_csv(REFERENCE_DIR / "conjunto_de_datos_enut_2024_thogar.csv")
    
#    )

"""
# 1. Para importar desde un archivo CSV
# df_cat_entidades = catálogo de entidades federativas
#df_cat_entidades = pd.read_csv('/Users/jorge/anaconda_projects/920a073c-2d0c-407c-9b32-c8476685090b/Datos/Datos/ModeloDatos/catalogos/cve_ent.csv')
df_cat_entidades = pd.read_csv('../Datos/Datos/ModeloDatos/catalogos/cve_ent.csv')
#df_cat_entidades = pd.read_csv('/Datos/Datos/ModeloDatos/catalogos/cve_ent.csv')
# df_cat_tam_pob = catálogo de tamaño de población de acuerdo al número de habitantes.
df_cat_tam_pob = pd.read_csv('../Datos/Datos/ModeloDatos/catalogos/menor10.csv')
# df_cat_respuesta = catálogo de pregunta si-no.
df_cat_respuesta = pd.read_csv('../Datos/Datos/ModeloDatos/catalogos/p2_4_01.csv')
# df_cat_respuesta_1 = catálogo de pregunta si-no-nosabe.
df_cat_respuesta_1 = pd.read_csv('../Datos/Datos/ModeloDatos/catalogos/p3_14_1.csv')
# df_cat_preguntas = catálogo de preguntas completas.
df_cat_preguntas = pd.read_csv('../Datos/Datos/ModeloDatos/diccionario_de_datos/diccionario_datos_enut_2024_thogar.csv')
# df_tabla_hogar = Tabla que contiene información relacionada con el hoghar .
df_tabla_hogar = pd.read_csv('../Datos/Datos/ModeloDatos/conjunto_de_datos/conjunto_de_datos_enut_2024_thogar.csv')
"""

#carga_df()


# In[9]:


# 3. Mostrar las primeras filas para verificar
#print(df_tabla_hogar.head())
# muestra todos los elementos de un dataframe
#print(df_cat_entidades)
# muestra los tipos de datos de un dataframe
#print(df_cat_entidades.dtypes)

# Mostramos solo la pregunta que queremos responder
#df_cat_preguntas_query = df_cat_preguntas.query("nemónico == 'p2_4_01'")
#print(df_cat_preguntas_query)
df_tabla_hogar_x_entidad = df_tabla_hogar.query("cve_ent == 15")
df_tabla_hogar_x_entidad_si = df_tabla_hogar.query("cve_ent == 15 and p2_4_01==1")
#print(df_tabla_hogar_x_entidad)
total_registros = len(df_tabla_hogar_x_entidad)
total_registros_si = len(df_tabla_hogar_x_entidad_si)


#A partir de la información comenzamos a responder preguntas
#¿Cuántos hogares tienen tv en el estado de México?
print(f"total de registros por estado, {total_registros}")
print(f"total de registros con tv por estado, {total_registros_si}")


# In[10]:


# 1. Definir los datos y las etiquetas
valores = [total_registros_si, total_registros - total_registros_si]
etiquetas = ['Viviendas con TV', 'Viviendas sin TV']

# 2. Crear el gráfico
plt.pie(valores, labels=etiquetas, autopct='%1.1f%%')

# 3. Mostrar la gráfica
plt.show()


# In[ ]:




