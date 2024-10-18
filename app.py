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
            # Recorre las respuestas para mostrar cada contenido en estilo LLM
            for item in response["value"]:
                content = item.get('content', 'Sin contenido')
                page = item.get('page', 'Sin página')
                url = item.get('url', None)  # El valor podría no estar presente

                # Verifica si el contenido es una tabla (lista de listas o lista de diccionarios)
                if isinstance(content, list):
                    try:
                        # Si es una lista de diccionarios, convertirlo a DataFrame
                        if all(isinstance(i, dict) for i in content):
                            df = pd.DataFrame(content)
                            st.table(df)
                        # Si es una lista de listas, manejarlo como DataFrame también
                        elif all(isinstance(i, list) for i in content):
                            df = pd.DataFrame(content)
                            st.table(df)
                        else:
                            st.markdown("Formato de tabla no reconocido.")
                    except Exception as e:
                        st.error(f"Error formateando la tabla: {e}")
                else:
                    # Si no es tabla, mostrar el contenido como texto en estilo LLM
                    st.markdown(f"**Respuesta:** {content}")
                
                # Mostrar la página asociada
                st.markdown(f"*Página asociada:* {page}")
                
                # Mostrar el enlace si está presente
                if url:
                    st.markdown(f"[Enlace asociado]({url})")
        else:
            st.warning("No se encontró 'value' en la respuesta JSON.")
    else:
        st.warning("Por favor, ingresa un mensaje.")
