from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# 📦 DATABASE SETUP
def init_db():
    conn = sqlite3.connect("history.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            text TEXT,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# 🧠 SMART NLP LOGIC
def analyze_text(text):
    text = text.lower()
    score = 0

    # 🚨 Strong danger words
    if any(word in text for word in ["kill", "attack", "explode"]):
        score += 1

    # ⚠️ Medium keyword
    if "bomb" in text:
        score += 0.6

        # 📍 Real-world context (important places)
        if any(word in text for word in ["hotel", "school", "airport", "bus", "station", "mall"]):
            score += 0.4   # increases seriousness

    # ✅ Safe/compliment context
    if any(word in text for word in ["look", "looking", "style", "awesome", "great", "cool", "beautiful"]):
        score -= 0.8

    # 🎯 FINAL DECISION
    if score >= 1:
        return "unsafe", "🚨 Unsafe Content", "#ef4444"
    elif score >= 0.5:
        return "uncertain", "⚠️ Suspicious Content", "#f59e0b"
    else:
        return "safe", "✅ Safe Content", "#22c55e"


# 🏠 HOME
@app.route("/")
def home():
    return render_template("index.html")


# 🔍 PREDICT
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({
            "status": "empty",
            "message": "Enter text",
            "color": "gray"
        })

    status, message, color = analyze_text(text)

    return jsonify({
        "status": status,
        "message": message,
        "color": color
    })


# 💾 SAVE HISTORY
@app.route("/save", methods=["POST"])
def save():
    data = request.get_json()
    user = data["user"]
    text = data["text"]
    status = data["status"]

    conn = sqlite3.connect("history.db")
    c = conn.cursor()
    c.execute("INSERT INTO history (user, text, status) VALUES (?, ?, ?)",
              (user, text, status))
    conn.commit()
    conn.close()

    return jsonify({"message": "Saved"})


# 📜 GET HISTORY
@app.route("/get_history")
def get_history():
    conn = sqlite3.connect("history.db")
    c = conn.cursor()
    c.execute("SELECT user, text, status FROM history ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()

    history = [{"user": r[0], "text": r[1], "status": r[2]} for r in rows]
    return jsonify(history)


# 🚀 RUN
if __name__ == "__main__":
    app.run(debug=True)