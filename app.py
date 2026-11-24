from flask import Flask, render_template, request, jsonify
import json
from pathlib import Path

app = Flask(__name__)
DATA = Path(__file__).parent / "data"

def load_json(name):
    with open(DATA / name, encoding="utf-8") as f:
        return json.load(f)

@app.route("/")
def home():
    return render_template("index.html", topics=load_json("topics.json"))

@app.route("/learn")
def learn():
    return render_template("learn.html", topics=load_json("topics.json"))

@app.route("/quiz")
def quiz():
    return render_template("quiz.html", questions=load_json("quiz.json"))

@app.route("/resources")
def resources():
    return render_template("resources.html", resources=load_json("resources.json"))

@app.route("/safety")
def safety():
    return render_template("safety.html")

@app.route("/api/quiz", methods=["POST"])
def grade_quiz():
    payload = request.get_json(silent=True) or {}
    answers = payload.get("answers", {})
    questions = load_json("quiz.json")
    score = sum(1 for q in questions if str(answers.get(str(q["id"]), "")) == str(q["answer"]))
    return jsonify({"score": score, "total": len(questions),
                    "message": "Great work! Review the explanations to strengthen your awareness." if score >= 7
                    else "Good attempt. Revisit the learning cards and try again."})

@app.errorhandler(404)
def not_found(_):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
