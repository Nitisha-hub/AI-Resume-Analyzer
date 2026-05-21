from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

# Local imports
from services.parser import extract_resume_text, analyze_resume

app = Flask(__name__)
CORS(app)

# ✅ Home route 
@app.route('/')
def home():
    return render_template('index.html')

# ✅ Resume upload route
@app.route('/upload', methods=['POST'])
def upload_resume():
    file = request.files['resume']

    # Extract text from PDF
    text = extract_resume_text(file)

    # Analyze resume
    analyzed_data = analyze_resume(text)

    # Return analysis result
    return jsonify(analyzed_data)

# ✅ History API (temporary)
@app.route('/history', methods=['GET'])
def get_history():
    return jsonify({"message": "History temporarily disabled"})

# ✅ Run app
if __name__ == '__main__':
    app.run(debug=True)
