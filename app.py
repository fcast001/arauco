from flask import Flask, request, jsonify, render_template
from chatbot_request import send_message_to_chatbot
import json

app = Flask(__name__)

def format_json(json_data):
    return json.dumps(json_data, indent=4, ensure_ascii=False)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    user_message = data.get("message")

    if not user_message:
        return jsonify({"error": "Missing message"}), 400

    api_key = "RVXAyI2OmGfbmgO8QtrUWUr2cv6Z3xLBCSsuoG5NisAzSeDBQdFm"  # Maneja esto de manera segura

    # Llama a la función que hace la solicitud al chatbot
    chatbot_response = send_message_to_chatbot(user_message, api_key)

    # Formatear la respuesta JSON
    formatted_response = format_json(chatbot_response)

    return jsonify({"formatted_response": formatted_response})

if __name__ == '__main__':
    app.run(debug=True)
