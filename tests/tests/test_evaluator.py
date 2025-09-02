import pytest
from evaluator import evaluate
from config import EVAL_CONFIG

def test_exact_match():
    result = evaluate("Hello World", "Hello World", EVAL_CONFIG)
    assert result["exact_match"] == 1.0
    assert result["final_score"] > 0.5

def test_word_overlap_partial():
    result = evaluate("Hello AI", "Hello World", EVAL_CONFIG)
    assert 0.0 <= result["word_overlap"] <= 1.0

def test_similarity():
    result = evaluate("Hello", "Helo", EVAL_CONFIG)
    assert result["similarity"] > 0.7

def test_missing_input():
    result = evaluate("", "Golden Answer", EVAL_CONFIG)
    assert result["final_score"] == 0.0
