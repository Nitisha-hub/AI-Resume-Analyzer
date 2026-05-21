from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from pymongo import MongoClient
import datetime

# Local imports
from services.parser import extract_resume_text, analyze_resume

app = Flask(__name__)
CORS(app)

# ✅ MongoDB Atlas connection
client = MongoClient("mongodb+srv://nitishamali23:resumepass123@resumeai-cluster.g39pi7j.mongodb.net/?retryWrites=true&w=majority&appName=ResumeAI-Cluster")
db = client["ResumeAnalyzer"]
collection = db["resumes"]

# ✅ Home route
@app.route('/')
def home():
    return render_template('index.html')

# ✅ Resume upload route
@app.route('/upload', methods=['POST'])
def upload_resume():
    file = request.files['resume']
    text = extract_resume_text(file)
    analyzed_data = analyze_resume(text)

    # Save to MongoDB
    analyzed_data["resume_text_preview"] = text[:1000]  # limit for testing
    analyzed_data["timestamp"] = datetime.datetime.now()
    collection.insert_one(analyzed_data)
    analyzed_data.pop("_id", None)  # safely remove _id before returning
    return jsonify(analyzed_data)


# ✅ History API
@app.route('/history', methods=['GET'])
def get_history():
    data = list(collection.find({}, {"_id": 0}))
    return jsonify(data)


# ✅ Run app
if __name__ == '__main__':
    app.run(debug=True)
