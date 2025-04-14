
---

```markdown
<p align="center">
  <a href="https://fastapi.tiangolo.com"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI"></a>
</p>
<p align="center">
    <em>FastAPI framework, high performance, easy to learn, fast to code, ready for production</em>
</p>

---

# 💡 Perspective-Driven Content Generation

This project implements an AI-powered service to generate **LinkedIn posts** for physicians that reflect their perspectives on healthcare AI topics. Built using **FastAPI** and integrated with **Google Vertex AI** (managed LLM service), the solution showcases prompt engineering and model alignment capabilities.

## 📌 Problem Statement

Develop an API that:
- Accepts an article summary or URL.
- Applies client-provided perspective statements.
- Generates a 200–250 word LinkedIn post reflecting a consistent tone: _“AI as enabler”_.
- Outputs a confidence score for alignment with the physician’s views.

---

## 🚀 Features

- ⚡ FastAPI backend for serving the model.
- 🔐 Google Vertex AI for text generation.
- 🧠 Prompt engineering layer for tone & viewpoint control.
- 📊 Confidence scoring system.
- 🧪 Includes 3 sample article tests.

---

## 🛠 Requirements

### Dependencies
Install with:

```bash
pip install -r requirements.txt
```

### Environment Setup

Generate and export your Google API key:

```bash
export GOOGLE_API_KEY=your_api_key_here
```

Make the shell script executable:

```bash
chmod +x entryPoint.sh
```

---

## ▶️ Running the Server

Start the server:

```bash
./entryPoint.sh
```

This uses:

```bash
fastapi dev main.py
```

Access the docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📂 Deliverables

- ✅ Working API (FastAPI + Vertex AI)
- ✅ Prompt Engineering Code (inside `services/prompt_engineering.py`)
- ✅ Confidence Score Logic (inside `utils/scoring.py`)
- ✅ 3 Sample Outputs (see `samples/`)
- ✅ Loom Video (link in submission)
- ✅ GitHub Repo (code under 25 lines)

---

## 📌 Notes

- The API is stateless and designed for easy deployment.
- Designed with flexibility for multi-LLM provider integration (Vertex AI used here).
- Limitations: Alignment is heuristic-based; could be improved with fine-tuning or RAG.

---

## 📄 License

This project is licensed under the MIT License.

```

--- 