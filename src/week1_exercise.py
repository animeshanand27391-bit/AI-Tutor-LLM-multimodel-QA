"""Multi-model Q&A: Ask one question, get answers from Claude, Gemini, Llama, and DeepSeek."""

from models import ask_claude, ask_deepseek, ask_gemini, ask_ollama
from utils import print_response

QUESTION = """
Please explain what this code does and why:
yield from {book.get("author") for book in books if book.get("author")}
"""


def main() -> None:
    print(f"Question:\n{QUESTION}")

    print_response("Anthropic Claude", ask_claude(QUESTION))
    print_response("Google Gemini", ask_gemini(QUESTION))
    print_response("Ollama (llama3.2)", ask_ollama(QUESTION))
    print_response("DeepSeek (deepseek-chat)", ask_deepseek(QUESTION))

    print()


if __name__ == "__main__":
    main()
