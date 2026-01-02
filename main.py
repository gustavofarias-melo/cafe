import os
from flask import Flask, request, jsonify, abort
from datetime import datetime

# Create Flask app
app = Flask(__name__)

# Set port and verify_token
PORT = int(os.environ.get("PORT", 3000))
VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN")

# Route for GET requests (webhook verification)
@app.route("/", methods=["GET"])
def verify_webhook():
    mode = request.args.get("hub.mode")
    challenge = request.args.get("hub.challenge")
    token = request.args.get("hub.verify_token")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK VERIFIED")
        return challenge, 200
    else:
        abort(403)

# Route for POST requests (receive webhook events)
@app.route("/", methods=["POST"])
def receive_webhook():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n\nWebhook received {timestamp}\n")
    print(request.get_json(indent=2, force=True))
    return "", 200

# Start the server
if __name__ == "__main__":
    print(f"\nListening on port {PORT}\n")
    app.run(host="0.0.0.0", port=PORT)
