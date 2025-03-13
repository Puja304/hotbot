import os
import json
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
INITIAL_RESPONSE = os.getenv("INITIAL_RESPONSE")
INITIAL_MSG = os.getenv("INITIAL_MSG")
CHAT_CONTEXT = os.getenv("CHAT_CONTEXT")

# Load case data
with open("case_data.json", "r") as json_file:
    case_details = json.load(json_file)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/guess')
def guess():
    return render_template('guess.html')

@app.route('/case_data')
def case_data():
    return jsonify(case_details)

if __name__ == "__main__":
    app.run(debug=True)