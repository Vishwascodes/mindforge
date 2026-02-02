def question_model(data):
    return {
        "question": data["question"],
        "options": data["options"],
        "answer": data["answer"],
        "difficulty": data["difficulty"],
        "category": data["category"]
    }

def user_model(username):
    return {
        "username": username,
        "score": 0,
        "level": "Beginner",
        "stats": {
            "logic": 0,
            "memory": 0,
            "math": 0,
            "pattern": 0
        }
    }
