# Setup Guide

## Prerequisites

- Python 3.12+
- [Ollama](https://ollama.com) installed locally
- API keys for Anthropic (required) and Google/OpenAI (optional)

## Step-by-Step

### 1. Clone & enter the project
```bash
git clone https://github.com/animeshanand27391-bit/llm-multimodel-qa.git
cd llm-multimodel-qa
```

### 2. Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate       # Mac/Linux
.venv\Scripts\activate          # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your API keys
```bash
cp .env.example .env
```
Open `.env` and fill in your keys:
```
ANTHROPIC_API_KEY=sk-ant-...
GOOGLE_API_KEY=AIza...
```

### 5. Pull the local Llama model
```bash
ollama pull llama3.2
```
Make sure Ollama is running:
```bash
ollama serve
```

### 6. Run the tool
```bash
python src/week1_exercise.py
```

## Troubleshooting

| Error | Fix |
|---|---|
| `ANTHROPIC_API_KEY is None` | Make sure `.env` exists and `load_dotenv()` runs first |
| `ollama: connection refused` | Run `ollama serve` in a separate terminal |
| `429 TooManyRequests` (Gemini) | Add `time.sleep(2)` between calls or use `gemini-1.5-flash` |
| `404` model not found | Run `ollama list` to see available local models |
