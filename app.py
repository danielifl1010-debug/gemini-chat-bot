from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Gemini Chat Bot is running!"

@app.route("/chat", methods=["POST"])
def chat():
    event = request.json

    message = event.get("message", {}).get("text", "")

    return jsonify({
        "text": f"קיבלתי: {message}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
