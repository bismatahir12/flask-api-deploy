from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask app deployed successfully on Vercel!'

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({
        "message": "Hello from your Flask API on Vercel!"
    })

if __name__ == '__main__':
    app.run(debug=True)
