from flask import Flask, jsonify
import os

app = Flask(__name__)

INSTANCE_ID = os.getenv("INSTANCE_ID", "0")

@app.route("/api/info")
def info():
    return jsonify({"instance_id": INSTANCE_ID})

@app.route("/health")
def health():
    return {
        "status": "ok",
        "instance": INSTANCE_ID
    }, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)