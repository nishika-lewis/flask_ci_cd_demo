from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to my Flask app!"

@app.route("/api/data")
def get_data():
    return jsonify({
        "name": "Nishika",
        "language": "Python",
        "status": "CI/CD is working 🎉"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
