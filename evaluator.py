from difflib import SequenceMatcher

def exact_match(model_answer: str, golden_answer: str) -> float:
    return 1.0 if model_answer.strip().lower() == golden_answer.strip().lower() else 0.0

def word_overlap(model_answer: str, golden_answer: str) -> float:
    model_words = set(model_answer.lower().split())
    golden_words = set(golden_answer.lower().split())
    if not golden_words:
        return 0.0
    return len(model_words & golden_words) / len(golden_words)

def similarity(model_answer: str, golden_answer: str) -> float:
    return SequenceMatcher(None, model_answer.lower(), golden_answer.lower()).ratio()

def evaluate(model_answer: str, golden_answer: str, config: dict) -> dict:
    scores = {
        "exact_match": exact_match(model_answer, golden_answer),
        "word_overlap": word_overlap(model_answer, golden_answer),
        "similarity": similarity(model_answer, golden_answer)
    }
    weighted_score = sum(scores[m] * config[f"{m}_weight"] for m in scores)
    scores["final_score"] = round(weighted_score, 2)
    return scores
