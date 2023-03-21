import streamlit as st
import random
from streamlit_card import card

def render_card(dict_recipes):

    col = st.columns(3)
    i = 0
    keys = list(dict_recipes.keys())
    random.shuffle(keys)
    for recipe in keys: 
        with col[i]:
            card(
                title=recipe,
                text=dict_recipes[recipe][0],
                image=dict_recipes[recipe][1],
                url=dict_recipes[recipe][2]
            )
        i+=1
        if(i == 3):
            return