# Medical Symptom Checker (LLM-powered Chatbot)

This is a full-stack AI-powered web application that allows users to describe their symptoms and receive general medical guidance. It integrates Azure OpenAI (ChatGPT) via a FastAPI backend and is built with Next.js 15 and TailwindCSS.

---

## Features

- Ask health-related questions in a chat-style interface
- AI responds with:
  - Possible conditions
  - At-home care tips
  - When to see a doctor
  - Urgent warning signs
- Chat history maintained in session
- Blocks unrelated or non-medical questions
- Fully responsive (mobile + desktop)
- Fast and clean UI with TailwindCSS

---

## Tech Stack

| Layer     | Technology     |
|-----------|----------------|
| Backend   | FastAPI (Python) |
| Frontend  | Next.js 15 (React) |
| Styling   | TailwindCSS |
| LLM API   | Azure OpenAI (ChatGPT) |

---

## Project Structure

medical-qa-assistant/
── backend/
  ── main.py
  ── schemas.py
  ── services.py
── frontend/
  ── app/
    ── page.tsx
  ── tailwind.config.ts
  ── ...


---

## Environment Variables

Create a .env file in the backend/ directory using this template:

AZURE_OPENAI_API_KEY=your-azure-openai-api-key
AZURE_OPENAI_ENDPOINT=https://lesha-pay-ai.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=gpt-4.1


---

## Setup Instructions

### Backend (FastAPI)
cd backend
python -m venv env
source env/bin/activate 
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload
Access API docs: http://localhost:8000/docs

## Frontend (Next.js)
Access API docs: http://localhost:8000/docs

Frontend (Next.js)
App will be available at: http://localhost:3000

# Prompt Engineering
Prompt used to guide the LLM:

You are a responsible medical assistant. A user describes these symptoms: '{symptoms}'.

Return the following:
1. Possible conditions (bullet list)
2. At-home care tips
3. When to see a doctor
4. Urgent warning signs

Do not diagnose. Keep advice general and educational.
    
# Limitation
Non-medical queries are rejected with an educational message.