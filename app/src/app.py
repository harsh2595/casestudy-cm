from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from CI/CD pipeline on EKS!"

@app.route("/health")
def health():
    return jsonify({"status": "UP"})
