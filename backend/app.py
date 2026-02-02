from flask import Flask, jsonify, request
from flask_cors import CORS
from database import questions_collection, users_collection
import random

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({"status": "Mind Forge API running"})


@app.route("/get-questions", methods=["GET"])
def get_questions():
    difficulty = request.args.get("difficulty")

    # If difficulty is provided → filter (case-insensitive)
    if difficulty:
        questions = list(
            questions_collection.find(
                {"difficulty": {"$regex": f"^{difficulty}$", "$options": "i"}},
                {"_id": 0}
            )
        )
    else:
        # If no difficulty provided → return all questions
        questions = list(questions_collection.find({}, {"_id": 0}))

    if not questions:
        return jsonify({
            "error": "No questions found"
        }), 404

    return jsonify(random.choice(questions))



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


