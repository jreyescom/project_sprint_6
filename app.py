import streamlit as st 
import pandas as pd
import plotly.express as px 

st.title("Anuncios de Autos en USA")
st.write("Datos de anuncios de venta de autos en Estados Unidos")

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
            
            
scratter_button = st.button('Construir gráfico de dispersión')
        
if scratter_button: # al hacer clic en el botón
    #escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
            
    #crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title='Gráfico de dispersión')
            
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)