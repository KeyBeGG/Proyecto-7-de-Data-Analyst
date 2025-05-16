import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') 

#Titulo de la aplicacion 
st.title("Mi primera app con Streamlit")
#Agregar un texto
st.write("Es una pagina web simple para aprobar el proyecto")
st.write("Usa el siguiente Boton para crear una histograma")

#Agrega un boton para crear un histograma simple
if st.button("Ver histograma"):
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    #Crear un histograma
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

st.write("Usa el siguiente Boton para crear un gráfico intereactivo")
#Agrega un boton para crear un gráfico intereactivo
if st.button("Ver gráfico"):
    st.write('Creación de un gráfico para el conjunto de datos de anuncios de venta de coches')
    #Mostrar un gráfico Plotly interactivo
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)