import streamlit as st
import requests

def send_message_to_chatbot(message, api_key):
    url = "https://search0-t4eqhr5zv6b54.search.windows.net/indexes/ragindex/docs/search?api-version=2021-04-30-Preview"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    payload = {
        "model": "gpt-3.5-turbo",  # Ajusta el modelo si es necesario
        "messages": [{"role": "user", "content": message}]
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        
        # Verifica si el código de estado es exitoso
        if response.status_code == 200:
            try:
                return response.json()  # Intenta decodificar la respuesta como JSON
            except requests.exceptions.JSONDecodeError:
                return {"error": "La respuesta no está en formato JSON."}
        else:
            return {"error": f"Error en la API: {response.status_code}", "details": response.text}
    except requests.exceptions.RequestException as e:
        return {"error": f"Error en la solicitud: {str(e)}"}

# Main Streamlit app
api_key = "RVXAyI2OmGfbmgO8QtrUWUr2cv6Z3xLBCSsuoG5NisAzSeDBQdFm"  # Maneja esto de manera segura

st.title("Chatbot LLM")

user_message = st.text_input("Escribe tu mensaje:")
if st.button("Enviar"):
    if user_message:
        response = send_message_to_chatbot(user_message, api_key)

        # Muestra la respuesta completa para inspección
        st.write("Respuesta completa de la API (texto):")
        st.write(response)  # Muestra la respuesta (en texto o JSON según el caso)
        
        # Verifica si la respuesta contiene el campo "choices"
        if "choices" in response and len(response["choices"]) > 0:
            # Extrae el texto de la respuesta
            llm_response = response["choices"][0]["message"]["content"]
            st.write("Respuesta del Chatbot:")
            st.write(llm_response)  # Muestra la respuesta del modelo LLM
        else:
            st.warning("No se encontró una respuesta válida en la respuesta JSON.")
    else:
        st.warning("Por favor, ingresa un mensaje.")
