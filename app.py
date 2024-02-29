import pandas as pd
import plotly.express as px
import streamlit as st
     
vehicles = pd.read_csv('C:\\Users\\carlo\\Documents\\_work\\TripleTen\\_codes\\notebook\\vehicles.csv') 
hist_button = st.button('Criar histograma') 
if hist_button:
     st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
     fig = px.histogram(vehicles, x="odometer")
     st.plotly_chart(fig, use_container_width=True)