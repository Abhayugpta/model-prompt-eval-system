from flask import Flask, request, jsonify
from evaluator import evaluate
from config import EVAL_CONFIG

app = Flask(__name__)

@app.route("/evaluate", methods=["POST"])
def evaluate_answer():
    data = request.get_json()
    model_answer = data.get("model_answer", "")
    golden_answer = data.get("golden_answer", "")

    if not model_answer or not golden_answer:
        return jsonify({"error": "Both model_answer and golden_answer are required"}), 400

    result = evaluate(model_answer, golden_answer, EVAL_CONFIG)
    return jsonify(result), 200

if __name__ == "__main__":
    app.run(debug=True)
