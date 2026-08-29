import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS

from ai_service import (
    explain_unsuitable_place,
    general_chat,
    generate_itinerary,
    recommend_places,
)
from database import get_db, init_db

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret-key")
CORS(app)

init_db()


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@app.route("/api/auth/register", methods=["POST"])
def register():
    data = request.get_json() or {}
    username = (data.get("username") or "").strip()
    email = (data.get("email") or "").strip().lower()

    if not username or not email:
        return jsonify({"error": "Username and email are required"}), 400

    conn = get_db()
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, email) VALUES (?, ?)",
            (username, email),
        )
        conn.commit()
        user_id = cursor.lastrowid
    except Exception:
        conn.close()
        return jsonify({"error": "Email already registered"}), 409
    conn.close()

    return jsonify({"id": user_id, "username": username, "email": email})


@app.route("/api/auth/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    username = (data.get("username") or "").strip()
    email = (data.get("email") or "").strip().lower()

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, username, email FROM users WHERE email = ? AND username = ?",
        (email, username),
    )
    user = cursor.fetchone()
    conn.close()

    if not user:
        return jsonify({"error": "Invalid credentials. Please register first."}), 401

    return jsonify({"id": user["id"], "username": user["username"], "email": user["email"]})


@app.route("/api/auth/google", methods=["POST"])
def google_login():
    data = request.get_json() or {}
    email = (data.get("email") or "").strip().lower()
    username = (data.get("username") or data.get("name") or "Google User").strip()
    google_id = data.get("googleId") or "demo-google"

    if not email:
        return jsonify({"error": "Google email required"}), 400

    conn = get_db()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, email FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()

        if not user:
            cursor.execute(
                "INSERT INTO users (username, email, google_id) VALUES (?, ?, ?)",
                (username, email, google_id),
            )
            conn.commit()
            user_id = cursor.lastrowid
            return jsonify({"id": user_id, "username": username, "email": email})
        else:
            return jsonify({"id": user["id"], "username": user["username"], "email": user["email"]})
    except Exception as e:
        return jsonify({"error": f"Google login failed: {str(e)}"}), 500
    finally:
        conn.close()


@app.route("/api/ai/plan-journey", methods=["POST"])
def plan_journey():
    data = request.get_json() or {}
    required = ["climate", "travelWith", "experience", "budget"]
    if not all(data.get(k) for k in required):
        return jsonify({"error": "All preference fields are required"}), 400

    result = recommend_places(data)
    return jsonify(result)


@app.route("/api/ai/unsuitable-place", methods=["POST"])
def unsuitable_place():
    data = request.get_json() or {}
    preferences = data.get("preferences") or {}
    place = (data.get("place") or "").strip()
    if not place:
        return jsonify({"error": "Place name required"}), 400
    result = explain_unsuitable_place(preferences, place)
    return jsonify(result)


@app.route("/api/ai/places-to-visit", methods=["POST"])
def places_to_visit():
    data = request.get_json() or {}
    place = (data.get("place") or "").strip()
    travel_with = data.get("travelWith") or "Solo"
    days = data.get("days") or 1

    if not place:
        return jsonify({"error": "Place is required"}), 400

    try:
        days = max(1, min(30, int(days)))
    except (TypeError, ValueError):
        days = 1

    result = generate_itinerary(place, travel_with, days)
    return jsonify(result)


@app.route("/api/ai/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    message = (data.get("message") or "").strip()
    if not message:
        return jsonify({"error": "Message required"}), 400
    result = general_chat(message, data.get("context"))
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, port=5000, use_reloader=False)
