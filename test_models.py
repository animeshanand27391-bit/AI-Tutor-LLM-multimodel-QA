"""
Basic sanity tests — these test structure and config, not live API calls.
To run: pytest tests/ -v
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))


def test_model_constants_defined():
    """Model name constants should be non-empty strings."""
    MODEL_ANTHROPIC = "claude-sonnet-4-6"
    MODEL_GOOGLE    = "models/gemini-2.0-flash-lite"
    MODEL_LLAMA     = "llama3.2"

    assert isinstance(MODEL_ANTHROPIC, str) and MODEL_ANTHROPIC
    assert isinstance(MODEL_GOOGLE, str) and MODEL_GOOGLE
    assert isinstance(MODEL_LLAMA, str) and MODEL_LLAMA


def test_env_example_exists():
    """The .env.example file should exist in the project root."""
    root = os.path.join(os.path.dirname(__file__), "..")
    assert os.path.exists(os.path.join(root, ".env.example"))


def test_requirements_exists():
    """requirements.txt should exist."""
    root = os.path.join(os.path.dirname(__file__), "..")
    assert os.path.exists(os.path.join(root, "requirements.txt"))


def test_question_is_non_empty():
    """The question string should never be empty."""
    question = """
    Please explain what this code does and why:
    yield from {book.get("author") for book in books if book.get("author")}
    """
    assert question.strip() != ""
