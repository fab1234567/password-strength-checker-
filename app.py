from flask import Flask, render_template, request
import re

app = Flask(__name__)

common_passwords = ["123456", "password", "qwerty", "admin"]

def check_password_strength(password):
    score = 0
    feedback = []

    if password in common_passwords:
        return "Very Weak ❌", ["Password is too common"]

    if len(password) < 8:
        feedback.append("Use at least 8 characters")
    else:
        score += 1

    if len(password) >= 12:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Add special characters")

    if score <= 2:
        strength = "Weak ❌"
    elif score <= 4:
        strength = "Medium ⚠️"
    else:
        strength = "Strong ✅"

    return strength, feedback


@app.route("/", methods=["GET", "POST"])
def index():
    strength = ""
    feedback = []

    if request.method == "POST":
        password = request.form["password"]
        strength, feedback = check_password_strength(password)

    return render_template("index.html", strength=strength, feedback=feedback)


if __name__ == "__main__":
    app.run(debug=True)
