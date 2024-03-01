import pandas as pd
import plotly.express as px
import streamlit as st
     
vehicles = pd.read_csv('vehicles.csv') 
hist_button = st.button('Criar histograma') 
scatter_button = st.button('Criar gráfico de dispersão')
if hist_button:
     st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
     fig = px.histogram(vehicles, x="odometer")
     st.plotly_chart(fig, use_container_width=True)

if scatter_button:
     st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
     fig = px.scatter(vehicles, x="odometer", y="price")
     st.plotly_chart(fig, use_container_width=True)