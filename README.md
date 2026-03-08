# LLM Multi-Model Q&A Tool

> Ask one question. Get answers from Claude, Gemini, Llama, and DeepSeek — side by side.

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)
![Anthropic](https://img.shields.io/badge/Claude-Sonnet_4.6-D97757?style=flat-square&logo=anthropic&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-2.0_Flash-4285F4?style=flat-square&logo=google&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Llama_3.2-000000?style=flat-square&logo=ollama&logoColor=white)
![DeepSeek](https://img.shields.io/badge/DeepSeek-Chat-6B4FBB?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## What This Does

Send a technical question to **four LLMs simultaneously** and compare their responses:

| Model | Provider | Cost |
|---|---|---|
| `claude-sonnet-4-6` | Anthropic | Pay per token |
| `gemini-2.0-flash-lite` | Google | Free tier available |
| `llama3.2` | Ollama (local) | 100% free |
| `deepseek-chat` | DeepSeek | Pay per token (very cheap) |

Built as part of a hands-on journey into LLM engineering — learning how different models think, respond, and reason.

---

## Quickstart

### 1. Clone the repo
```bash
git clone https://github.com/animeshanand27391-bit/AI-Tutor-LLM-multimodel-QA.git
cd AI-Tutor-LLM-multimodel-QA
```

### 2. Set up your environment
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure API keys
```bash
cp .env.example .env
# Edit .env and add your keys
```

### 4. Pull the local model
```bash
ollama pull llama3.2
```

### 5. Run it
```bash
# As a script
python src/week1_exercise.py

# Or open the notebook
jupyter notebook notebooks/week1_EXERCISE.ipynb
```

---

## Project Structure

```
AI-Tutor-LLM-multimodel-QA/
├── src/
│   ├── week1_exercise.py     # Main multi-model Q&A script
│   ├── models.py             # Model client wrappers
│   └── utils.py              # Shared helpers
├── notebooks/
│   └── week1_EXERCISE.ipynb  # Interactive Jupyter version
├── tests/
│   └── test_models.py        # Unit tests
├── .github/
│   └── workflows/
│       └── ci.yml            # GitHub Actions CI
├── .env.example              # API key template
├── .gitignore                # Ignores secrets & cache
├── MODELS.md                 # Model comparison & notes
├── SETUP.md                  # Detailed setup guide
├── requirements.txt          # Python dependencies
└── pyproject.toml            # Project metadata
```

---

## API Keys Needed

| Key | Where to get it | Required? |
|---|---|---|
| `ANTHROPIC_API_KEY` | [console.anthropic.com](https://console.anthropic.com) | Yes |
| `GOOGLE_API_KEY` | [aistudio.google.com](https://aistudio.google.com) | Optional |
| `DEEPSEEK_API_KEY` | [platform.deepseek.com](https://platform.deepseek.com) | Optional |

Ollama runs **100% locally** — no API key needed.

---

## Example Output

```
Question:
Please explain what this code does and why:
yield from {book.get("author") for book in books if book.get("author")}

------------------------------------------------------------
  Anthropic Claude
------------------------------------------------------------
This code uses a generator to yield unique authors from a
list of books, filtering out any books without an author...

------------------------------------------------------------
  Google Gemini
------------------------------------------------------------
The expression combines a set comprehension with yield from...

------------------------------------------------------------
  Ollama (llama3.2)
------------------------------------------------------------
This is a Python generator expression that...

------------------------------------------------------------
  DeepSeek (deepseek-chat)
------------------------------------------------------------
This yields unique, non-null authors from the books list...
```

---

## Roadmap

- [x] Multi-model Q&A (Claude + Gemini + Llama + DeepSeek)
- [ ] Streaming responses
- [ ] Side-by-side web UI (Gradio / Streamlit)
- [ ] Add Groq support
- [ ] Evaluation framework — score model responses
- [ ] RAG pipeline integration

---

## About

Built by **Animesh Anand** — Sr. Security Engineer entering the AI/LLM space.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/animesh-anand27)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/animeshanand27391-bit)

---

## License

MIT — see [LICENSE](LICENSE) for details.
