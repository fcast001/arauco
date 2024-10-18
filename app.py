import streamlit as st
from chatbot_request import send_message_to_chatbot

api_key = "RVXAyI2OmGfbmgO8QtrUWUr2cv6Z3xLBCSsuoG5NisAzSeDBQdFm"  # Maneja esto de manera segura

st.title("Chatbot")

user_message = st.text_input("Escribe tu mensaje:")
if st.button("Enviar"):
    if user_message:
        response = send_message_to_chatbot(user_message, api_key)

        # Verifica si la respuesta contiene un valor
        if "value" in response:
            # Recorre las respuestas para mostrar cada contenido en estilo LLM
            for item in response["value"]:
                content = item.get('content', 'Sin contenido')
                page = item.get('page', 'Sin página')
                url = item.get('url', 'Sin URL')

                # Formatear la respuesta para que se vea como un LLM
                st.markdown(f"*Respuesta:* {content}")
                st.markdown(f"*Página asociada:* {page}")
                st.markdown(f"[Enlace asociado]({url})")
        else:
            st.warning("No se encontró 'value' en la respuesta JSON.")
    else:
        st.warning("Por favor, ingresa un mensaje.")
