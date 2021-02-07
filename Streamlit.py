import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Título de prueba')
st.write('Prueba')
df=pd.read_excel('MIBGAS.xlsx',sheet_name='Mensual',index_col=0)
indices=['Indice MIBGAS [EUR/MWh]', 'Indice MIBGAS-LNG [EUR/MWh]',
       'Volumen MIBGAS [MWh]', 'Volumen MIBGAS-LNG [MWh]']

indice_select=st.selectbox('Índices',indices)

figura,ax=plt.subplots()
ax.plot(df[indice_select])
plt.show()

# st.table(df)
st.pyplot(fig=figura)
