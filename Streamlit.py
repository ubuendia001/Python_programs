import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

@st.cache()
def coger_datos():
    datos=pd.read_excel('Datos.xlsx')
    return datos
df=coger_datos()
# columnas=['valor', 'Año', 'País', 'Tipo']
paises=df['País'].unique()

st.title('OBJETIVOS DE EFIENCIA ENERGÉTICA DE LA UE')
st.write("The European Union (EU) has committed itself to a 20 % reduction of energy consumption by the year 2020 compared to baseline[1] projections. This objective is also known as the 20 % energy efficiency target. In other words, the EU has committed[2] itself to have a primary energy consumption of no more than 1 483 Mtoe and a final energy consumption of no more than 1 086 Mtoe in 2020. For 2030 the binding target is at least 32.5 % reduction. This translates into a primary energy consumption of no more than 1 273 Mtoe and a final energy consumption of no more than 956 Mtoe in 2030. With the withdrawal of the United Kingdom, the Union's energy consumption figures for 2020 and 2030 needs to be adjusted to the situation of 27 Member States. A technical adaptation of targets results in a primary energy consumption of no more than 1 312 Mtoe in 2020 and 1 128 Mtoe in 2030 and a final energy consumption of no more than 959 Mtoe in 2020 and 846 Mtoe in 2030.")
region=st.selectbox('Región',paises)
mostrar=df[df['País']==region].pivot_table(index='Año',columns='Tipo',values='valor',aggfunc='sum')
mostrar['Objetivo final 2020']=mostrar['Consumo final']-mostrar['Consumo final distancia 2020']
mostrar['Objetivo final 2030']=mostrar['Consumo final']-mostrar['Consumo final distancia 2030']
mostrar['Objetivo primario 2020']=mostrar['Consumo primario']-mostrar['Consumo primario distancia 2020']
mostrar['Objetivo primario 2030']=mostrar['Consumo primario']-mostrar['Consumo primario distancia 2030']
st.table(round(mostrar,2))

descargar_tabla=st.button('Descargar tabla')
if descargar_tabla==True:
    st.write('Descargando tabla...')
    tabla.to_excel('Tabla descagarda.xlsx')
    st.write('Tabla descargada')

tipo=st.selectbox('Indicador',['final','primario'])

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

descargar_grafico=st.button('Descargar gráfico')
if descargar_grafico==True:
    st.write('Descargando imagen...')
    plt.tight_layout()
    plt.savefig(region+'_'+tipo+'.png',dpi=300)
    st.write('Imagen descargada')

