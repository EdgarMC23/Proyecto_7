import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
st.header("Analisis de venta de coches")  # Encabezado
# Botón de histograma
hist_button = st.button('Construir histograma')
# Botón de grafico de dispersion
disp_button = st.button("Construir gráfico de dispersión")

if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig_hist = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)


if disp_button:
    st.write("Creación de grafico de dispersión para el conjunto de datos de anuncios de venta de coches")

    # crear grafico de dispersión
    fig_disp = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_disp, use_container_width=True)
