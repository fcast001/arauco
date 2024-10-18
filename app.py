import streamlit as st
import pandas as pd
import requests

def send_message_to_chatbot(message, api_key):
    url = "https://search0-t4eqhr5zv6b54.search.windows.net/indexes/ragindex/docs/search?api-version=2021-04-30-Preview"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    payload = {
        "model": "gpt-3.5-turbo",  # Puedes elegir otro modelo si lo prefieres
        "messages": [{"role": "user", "content": message}]
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()  # Devuelve la respuesta en formato JSON
    else:
        return {"error": response.text}

# Main Streamlit app
api_key = "RVXAyI2OmGfbmgO8QtrUWUr2cv6Z3xLBCSsuoG5NisAzSeDBQdFm"  # Maneja esto de manera segura

st.title("Chatbot LLM")

user_message = st.text_input("Escribe tu mensaje:")
if st.button("Enviar"):
    if user_message:
        response = send_message_to_chatbot(user_message, api_key)

        # Verifica si la respuesta contiene un valor
        if "choices" in response and len(response["choices"]) > 0:
            # Extrae el texto de la respuesta
            llm_response = response["choices"][0]["message"]["content"]
            st.write("Respuesta del Chatbot:")
            st.write(llm_response)  # Muestra la respuesta del modelo LLM
        else:
            st.warning("No se encontró respuesta en la respuesta JSON.")
    else:
        st.warning("Por favor, ingresa un mensaje.")
