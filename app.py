from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# Load Q&A from the JSON file
def load_data():
    try:
        with open(os.path.join('static', 'data.json')) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

data = load_data()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json.get('question')
    response = "Sorry, I don't have an answer for that."

    if not data:
        return jsonify({'response': "Sorry, I don't have any data available."})

    for key, answer in data.items():
        if key.lower() in question.lower():
            response = answer
            break

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
