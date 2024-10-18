import streamlit as st
import pandas as pd
from chatbot_request import send_message_to_chatbot

api_key = "RVXAyI2OmGfbmgO8QtrUWUr2cv6Z3xLBCSsuoG5NisAzSeDBQdFm"  # Maneja esto de manera segura

st.title("Chatbot")

user_message = st.text_input("Escribe tu mensaje:")
if st.button("Enviar"):
    if user_message:
        response = send_message_to_chatbot(user_message, api_key)

        # Verifica si la respuesta contiene un valor
        if "value" in response:
            # Convierte la lista de objetos en un DataFrame
            response_df = pd.json_normalize(response["value"])  # Normaliza la respuesta JSON
            st.dataframe(response_df)  # Muestra la respuesta en una tabla
        else:
            st.warning("No se encontró 'value' en la respuesta JSON.")
    else:
        st.warning("Por favor, ingresa un mensaje.")
