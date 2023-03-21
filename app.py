import streamlit as st
from ferramentas import get_ip, get_region, weather_api, get_partDay
from datetime import date, datetime
from modelo.arvore_decisao import predicao
from ferramentas.receitas_api import get_recipe
from ferramentas.render_cards import render_card

# informações de contexto

weekday_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

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

st.title('Recipe Now')

parametros = {"Região": region, "Estado": state, 
            "Temperatura": temp, "Tempo": weather, 
            "Estação": station, "Período do dia": partOfDay, 
            "Dia da Semana": weekday}

st.caption("Context Info:  " + str(parametros))

user_search = st.text_input('Search for a recipe', placeholder="Insert keyword")

user_predict = predicao([region, state, temp, weather, station, partOfDay, weekday])

recipes = get_recipe(user_predict)

if user_search:
    user_recipes = get_recipe(user_search)
    if user_recipes:
        st.subheader("Your Results")
        render_card(user_recipes)
    else:
        st.caption('No Results')
        st.subheader("Recomendation for you")
        render_card(recipes)
else:
    st.subheader("Recomendation for you")
    render_card(recipes)