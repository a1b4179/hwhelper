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
        'message': 'HWHelper API',
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
        
        # Simple demo response
        solution = f"# {subject} Solution\n\n## Your Question:\n{question}\n\n## Answer:\nThis is a demo response. API is working!\n\nNext we'll add AI agents."
        
        return jsonify({
            'success': True,
            'solution': solution
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
