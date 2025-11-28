from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="*")

@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    return response

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': '🎓 HWHelper API',
        'status': 'online'
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

@app.route('/solve', methods=['POST', 'OPTIONS'])
def solve():
    if request.method == 'OPTIONS':
        return jsonify({'status': 'ok'}), 200
    
    try:
        data = request.json
        question = data.get('question', '')
        subject = data.get('subject', 'General')
        
        # Simple response for now (we'll add AI later)
        solution = f"""# {subject} Solution

## Your Question:
{question}

## Answer:
This is a demo response. We'll connect the AI agents next!
