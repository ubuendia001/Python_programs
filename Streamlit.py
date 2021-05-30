import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

@st.cache()
def coger_datos():
    datos=pd.read_excel('Datos.xlsx')
    return datos
df=coger_datos()
paises=df['País'].unique()

st.title('OBJETIVOS DE EFIENCIA ENERGÉTICA DE LA UE')
st.write("The European Union (EU) has committed itself to a 20 % reduction of energy consumption by the year 2020 compared to baseline[1] projections. This objective is also known as the 20 % energy efficiency target. In other words, the EU has committed[2] itself to have a primary energy consumption of no more than 1 483 Mtoe and a final energy consumption of no more than 1 086 Mtoe in 2020. For 2030 the binding target is at least 32.5 % reduction. This translates into a primary energy consumption of no more than 1 273 Mtoe and a final energy consumption of no more than 956 Mtoe in 2030. With the withdrawal of the United Kingdom, the Union's energy consumption figures for 2020 and 2030 needs to be adjusted to the situation of 27 Member States. A technical adaptation of targets results in a primary energy consumption of no more than 1 312 Mtoe in 2020 and 1 128 Mtoe in 2030 and a final energy consumption of no more than 959 Mtoe in 2020 and 846 Mtoe in 2030.")
region=st.selectbox('Región',paises)
tipo=st.selectbox('Indicador',['final','primario'])

mostrar=df[df['País']==region].pivot_table(index='Año',columns='Tipo',values='valor',aggfunc='sum')
mostrar['Objetivo final 2020']=mostrar['Consumo final']-mostrar['Consumo final distancia 2020']
mostrar['Objetivo final 2030']=mostrar['Consumo final']-mostrar['Consumo final distancia 2030']
mostrar['Objetivo primario 2020']=mostrar['Consumo primario']-mostrar['Consumo primario distancia 2020']
mostrar['Objetivo primario 2030']=mostrar['Consumo primario']-mostrar['Consumo primario distancia 2030']
if tipo=='final':
    st.write('Objetivo consumo final 2020: {:.0f} Mtep'.format(mostrar['Objetivo final 2020'].mean()))
    st.write('Objetivo consumo final 2030: {:.0f} Mtep'.format(mostrar['Objetivo final 2030'].mean()))
elif tipo=='primario':
    st.write('Objetivo consumo primario 2020: {:.0f} Mtep'.format(mostrar['Objetivo primario 2020'].mean()))
    st.write('Objetivo consumo primario 2030: {:.0f} Mtep'.format(mostrar['Objetivo primario 2030'].mean()))
# mostrar.drop(columns=['Objetivo final 2020','Objetivo final 2030','Objetivo primario 2020','Objetivo primario 2030'],inplace=True)


x=mostrar.index.values
y=mostrar['Consumo '+tipo].values
objetivo_2020=mostrar['Objetivo '+tipo+' 2020'].mean()
objetivo_2030=mostrar['Objetivo '+tipo+' 2030'].mean()

figura=plt.figure()
plt.plot(x,y,color='skyblue')
plt.hlines(y=objetivo_2020,linestyle='dashed',color='salmon',xmin=1990,xmax=2020)
plt.hlines(y=objetivo_2030,linestyle='dashed',color='darkgreen',xmin=1990,xmax=2030)
plt.xlim(1990,2030)
plt.title('Consumo '+tipo+' (Mtep)\n'+region)
st.pyplot(figura)

st.table(round(mostrar,0))

import base64
def crear_link(df, archivo_nombre,etiqueta):
    object_to_download = df.to_csv(index=False)
    b64 = base64.b64encode(object_to_download.encode()).decode()
    return f'<a href="data:file/txt;base64,{b64}" download="{archivo_nombre}">{etiqueta}</a>'

link = crear_link(mostrar, 'Descarga.csv','Descargar csv')
st.markdown(link, unsafe_allow_html=True)

