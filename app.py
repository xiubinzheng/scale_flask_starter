"""Minimal Flask API for the Scale AI coding interview."""

from flask import Flask, request

app = Flask(__name__)


@app.get("/hello_world")
def hello_world():
    return {"hello": "world"}, 200


@app.post("/echo")
def echo():
    """Tiny example of accepting and returning JSON; not an interview solution."""
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return {"error": "Expected a JSON object"}, 400
    return {"received": payload}, 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
