"""Model client wrappers for Anthropic, Google Gemini, and Ollama."""

import os

import anthropic
import google.generativeai as genai
import ollama as ollama_client
from dotenv import load_dotenv

load_dotenv()

MODEL_ANTHROPIC = "claude-sonnet-4-6"
MODEL_GOOGLE = "models/gemini-2.0-flash-lite"
MODEL_LLAMA = "llama3.2"


def ask_claude(question: str) -> str:
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    response = client.messages.create(
        model=MODEL_ANTHROPIC,
        max_tokens=1024,
        messages=[{"role": "user", "content": question}],
    )
    return response.content[0].text


def ask_gemini(question: str) -> str:
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
    model = genai.GenerativeModel(MODEL_GOOGLE)
    response = model.generate_content(question)
    return response.text


def ask_ollama(question: str) -> str:
    response = ollama_client.chat(
        model=MODEL_LLAMA,
        messages=[{"role": "user", "content": question}],
    )
    return response["message"]["content"]
