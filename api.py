from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import dotenv_values
from groq import Groq

app = Flask(__name__)
CORS(app)  # Allows frontend to communicate with backend

# Load API key
secrets = dotenv_values(".env")
GROQ_API_KEY = secrets["GROQ_API_KEY"]
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

client = Groq()

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message", "")

    messages = [
        {"role": "system", "content": secrets["CHAT_CONTEXT"]},
        {"role": "assistant", "content": secrets["INITIAL_MSG"]},
        {"role": "user", "content": user_message},
    ]

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        stream=False  # Disable streaming for API response
    )

    return jsonify({"reply": response.choices[0].message.content})

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Run on port 5000
