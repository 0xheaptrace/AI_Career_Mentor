import os
import json
import requests
import time

PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")
API_URL = "https://api.perplexity.ai/chat/completions"


def chat_llm(chat_history, resume_text, typed_skills, domain, role, required_skills, retries=2):
    system_prompt = f"""
You are a friendly AI career mentor.

You help students understand:
- What they are good at
- What skills they are missing
- What they should learn next
- Career guidance based on conversation

Context:
Domain: {domain}
Role: {role}
Required Skills: {required_skills}

Resume Text:
{resume_text}

User Typed Skills:
{typed_skills}

Rules:
- Talk naturally like a mentor
- Be encouraging
- If user asks about skills, analyze gaps
- If user asks general questions, answer conversationally
"""

    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(chat_history)

    headers = {
        "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "sonar-pro",
        "messages": messages,
        "temperature": 0.4
    }

    for _ in range(retries):
        try:
            r = requests.post(API_URL, headers=headers, json=payload, timeout=30)
            if r.status_code == 200:
                return r.json()["choices"][0]["message"]["content"]
            time.sleep(1)
        except Exception:
            time.sleep(1)

    return "⚠️ AI is temporarily unavailable. Please try again."
