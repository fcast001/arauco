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
            
            # Selecciona las columnas que deseas mostrar
            selected_columns = ['content', 'page', 'url']  # Cambia esto según tus necesidades
            if all(col in response_df.columns for col in selected_columns):
                # Formatea los enlaces como hipervínculos
                response_df['url'] = response_df['url'].apply(lambda x: f'<a href="{x}" target="_blank">{x}</a>')
                
                # Muestra el DataFrame, convirtiendo la columna de enlaces
                st.markdown(response_df.to_html(escape=False), unsafe_allow_html=True)
            else:
                st.warning("No se encontraron las columnas seleccionadas en la respuesta.")
        else:
            st.warning("No se encontró 'value' en la respuesta JSON.")
    else:
        st.warning("Por favor, ingresa un mensaje.")
