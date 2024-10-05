from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import AutoModelForCausalLM, AutoTokenizer

app = Flask(__name__)

# Enable CORS with explicit settings
cors = CORS(app, resources={r"/*": {"origins": "https://chshankar19.github.io"}}, supports_credentials=True)

# Load the model
model_name = "EleutherAI/gpt-neo-1.3B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=150)
    response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response_text

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    prompt = data.get('prompt')
    response = generate_response(prompt)
    return jsonify({'response': response})

# Explicitly handle OPTIONS request (preflight)
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'https://chshankar19.github.io')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
