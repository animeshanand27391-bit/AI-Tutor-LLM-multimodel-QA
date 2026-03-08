# Model Reference

## Models Used

### Anthropic Claude — `claude-sonnet-4-6`
- **Type:** Cloud API
- **Strengths:** Reasoning, code explanation, long context
- **Response syntax:** `response.content[0].text`
- **Docs:** https://docs.anthropic.com

### Google Gemini — `models/gemini-2.0-flash-lite`
- **Type:** Cloud API (free tier available)
- **Strengths:** Fast, multimodal, generous free limits
- **Response syntax:** `response.text`
- **Free limits:** 30 req/min, 1500 req/day
- **Docs:** https://aistudio.google.com

### Ollama / Llama 3.2 — `llama3.2`
- **Type:** Local (runs on your machine)
- **Strengths:** 100% free, no rate limits, fully private
- **Response syntax:** `response["message"]["content"]`
- **Docs:** https://ollama.com

### DeepSeek — `deepseek-chat`
- **Type:** Cloud API (via OpenAI-compatible wrapper)
- **Strengths:** Strong reasoning, very low cost
- **Response syntax:** `response.choices[0].message.content`
- **Docs:** https://platform.deepseek.com/docs

---

## Response Syntax Cheat Sheet

| Provider   | Client call                           | Get text                               |
|------------|---------------------------------------|----------------------------------------|
| Anthropic  | `client.messages.create(...)`         | `response.content[0].text`             |
| Gemini     | `model.generate_content(...)`         | `response.text`                        |
| Ollama     | `ollama_client.chat(...)`             | `response["message"]["content"]`       |
| DeepSeek   | `client.chat.completions.create(...)` | `response.choices[0].message.content`  |

---

## Cost & Availability Comparison

| Model | Free? | Rate Limit | Best For |
|---|---|---|---|
| `claude-sonnet-4-6` | Pay per token | Generous | Reasoning, code |
| `gemini-2.0-flash-lite` | Free tier | 30 req/min | General use |
| `llama3.2` (Ollama) | 100% free | No limit | Local, private |
| `deepseek-chat` (Cloud) | Pay per token (cheap) | Per plan | Cost-efficient reasoning |
