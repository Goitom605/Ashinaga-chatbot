
from flask import Flask, render_template, request, jsonify, session
from models.user_model import create_user, verify_user
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = "supersecretkey"

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


# Home route
@app.route("/")
def home():
    return render_template("index.html")



# Logout route
@app.route("/logout")
def logout():
    session.clear()
    return jsonify({"message": "Logged out successfully"})


# Registeration route
@app.route("/register", methods=["POST"])
def register():
    data = request.json

    username = data["username"]
    email = data["email"]
    password = data["password"]

    create_user(username, email, password)

    return jsonify({"message": "You registered successfully"})


# Login route
@app.route("/login", methods=["POST"])
def login():
    data = request.json

    email = data["email"]
    password = data["password"]

    user = verify_user(email, password)

    if user:
        session["user_id"] = user[0]
        session["username"] = user[1]

        return jsonify({"message": "Login successful", "username": user[1]})

    return jsonify({"message": "Invalid credentials"}), 401


@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json.get("message")

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are Ashinaga AI Assistant. "
                    "Help users with scholarships, applications, education, mission, vision, and founder information. "
                    "Be clear, helpful, and slightly formal. Also, try to give accurate information"
                )
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

# find the model's response inside the nested dictionary
    reply = response.json()["choices"][0]["message"]["content"]

# change the reply into python dictionary and return it to the browser
    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)