import streamlit as st
import pandas as pd
import numpy as np
from streamlit_card import card
from ferramentas import get_ip, get_region, weather_api, get_partDay
from datetime import date, datetime

# informações de contexto

weekday_list = ['segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']

state, lat, lon = get_ip.get_ip()

region = get_region.consulta_regiao(state)

weather, temp = weather_api.get_weather(lat, lon)

current_date = date.today()

weekday = weekday_list[current_date.weekday()]

current_time = datetime.now()

current_hour = current_time.hour
partOfDay = get_partDay.get_partDay(current_hour)

station = get_partDay.get_station(current_time)


# Página

st.title('Receitas Já!')

parametros = {"Região": region, "Estado": state, 
            "Temperatura": temp, "Tempo": weather, 
            "Estação": station, "Período do dia": partOfDay, 
            "Dia da Semana": weekday}

st.caption("Informações de contexto:  " + str(parametros))

title = st.text_input('Pesquise uma receita', placeholder="Insira aqui uma palavra-chave")

st.subheader("Recomendados para você com base nas suas informações")

col = st.columns(3)

for i in range(3): 
    with col[i]:
        card(
            title=str(i),
            text="This is a test card",
            image="https://placekitten.com/500/500",
            url="https://github.com/gamcoh/st-card",
        )

# st.write(res)   
# st.write(res) 