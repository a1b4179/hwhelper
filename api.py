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

Your homework solver is working! 🎉

## Next Steps:
1. The API is connected ✅
2. We'll add AI agents next
3. Then add video search
"""
        
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
```

4. Click **"Commit changes"**

---

### **Step 3: Deploy to Render**

1. Go to: https://render.com
2. Click **"Get Started"** or **"Sign Up"**
3. Sign up with **GitHub**
4. After login, click **"New +"** → **"Web Service"**
5. Click **"Connect"** next to your `hwhelper` repository
6. Fill in:
   - **Name:** `hwhelper`
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn api:app`
7. Click **"Create Web Service"**

**Wait 5 minutes...** Render is deploying!

---

### **Step 4: Get Your API URL**

1. After deploy finishes, you'll see a URL like:
```
   https://hwhelper-abc123.onrender.com
```
2. **COPY THIS URL!** Write it down!

---

### **Step 5: Test Your API**

Open this in your browser:
```
https://YOUR-RENDER-URL.onrender.com/health
