import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Título de prueba')
st.write('Prueba')
df=pd.read_excel('MIBGAS.xlsx',sheet_name='Mensual',index_col=0)
st.table(df)

indices=['Indice MIBGAS [EUR/MWh]', 'Indice MIBGAS-LNG [EUR/MWh]',
       'Volumen MIBGAS [MWh]', 'Volumen MIBGAS-LNG [MWh]']

indice_select=st.selectbox('Índices',indices)

figura=plt.figure()
plt.plot(df.loc[:,indice_select])


st.pyplot(fig=figura)
