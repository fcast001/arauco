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
            
            # Selecciona solo las columnas que deseas mostrar
            selected_columns = ['content', 'page', 'url']  # Cambia esto según tus necesidades
            
            # Verifica que las columnas seleccionadas existen en el DataFrame
            existing_columns = [col for col in selected_columns if col in response_df.columns]
            
            # Crea un nuevo DataFrame con las columnas seleccionadas
            selected_df = response_df[existing_columns].copy()
            
            # Formatea los enlaces como hipervínculos
            if 'url' in selected_df.columns:
                selected_df['url'] = selected_df['url'].apply(lambda x: f'<a href="{x}" target="_blank">{x}</a>')
            
            # Muestra el DataFrame con columnas seleccionadas usando st.markdown
            st.markdown(selected_df.to_html(escape=False), unsafe_allow_html=True)
        else:
            st.warning("No se encontró 'value' en la respuesta JSON.")
    else:
        st.warning("Por favor, ingresa un mensaje.")
