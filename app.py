import streamlit as st
import pandas as pd
import openai

# Configura tu API key
api_key = "RVXAyI2OmGfbmgO8QtrUWUr2cv6Z3xLBCSsuoG5NisAzSeDBQdFm"  # Maneja esto de manera segura

# Función para generar respuestas del modelo LLM
def generate_llm_response(prompt, api_key):
    openai.api_key = api_key
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Cambia esto al modelo que prefieras
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"Error: {str(e)}"

# Función para enviar el mensaje al chatbot
def send_message_to_chatbot(message, api_key):
    url = "https://search0-t4eqhr5zv6b54.search.windows.net/indexes/ragindex/docs/search?api-version=2021-04-30-Preview"
    headers = {
        'Content-Type': 'application/json',
        'api-key': api_key
    }
    payload = {
        "search": message,
        "top": 5
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}

# Título de la aplicación
st.title("Chatbot LLM")

# Entrada de texto del usuario
user_message = st.text_input("Escribe tu mensaje:")
if st.button("Enviar"):
    if user_message:
        # Genera la respuesta usando el modelo LLM
        llm_response = generate_llm_response(user_message, api_key)
        
        # Muestra la respuesta del modelo LLM
        st.write("Respuesta del LLM:")
        st.write(llm_response)

        # Llama al chatbot
        response = send_message_to_chatbot(user_message, api_key)
        
        # Verifica si "value" está en la respuesta
        if "value" in response:
            # Convierte la lista de objetos en un DataFrame
            response_df = pd.json_normalize(response["value"])  # Normaliza la respuesta JSON
            
            # Selecciona columnas específicas si es necesario
            selected_columns = ['column1', 'column2', 'url']  # Reemplaza con los nombres de las columnas que desees mostrar
            response_df = response_df[selected_columns]  # Filtra las columnas seleccionadas
            
            # Muestra la respuesta en una tabla
            st.dataframe(response_df)  # Muestra la respuesta en una tabla
        else:
            st.warning("No se encontró 'value' en la respuesta JSON.")
    else:
        st.warning("Por favor, ingresa un mensaje.")
