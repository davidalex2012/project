import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.checkbox('Construir histograma') # crear botón para histograma
plot_button = st.checkbox('Construir gráfico de dispersión') #crear botón para plot

st.header('Presiona un botón para construir un histograma o gráfico de dispersión')

if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if plot_button: # hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

            # crear un gráfico de dispersión
    fig = px.scatter (car_data, x = 'odometer', y = 'price')

            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


