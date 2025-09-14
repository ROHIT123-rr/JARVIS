import json
import requests
from typing import Optional
from config import OPENROUTER_API_KEY, OPENROUTER_URL, OPENROUTER_MODEL, HTTP_REFERER, APP_TITLE


def chat(prompt: str) -> Optional[str]:
    if not OPENROUTER_API_KEY:
        return "OpenRouter API key is missing. Please set OPENROUTER_API_KEY."

    # Try multiple free models
    models_to_try = [
        "meta-llama/llama-3.1-8b-instruct:free",
        "microsoft/phi-3-mini-128k-instruct:free", 
        "google/gemma-2-9b-it:free",
        "deepseek/deepseek-r1:free"
    ]

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "HTTP-Referer": HTTP_REFERER,
        "Referer": HTTP_REFERER,
        "X-Title": APP_TITLE,
    }
    
    for model in models_to_try:
        data = {
            "model": model,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are Jarvis, a concise personal assistant. "
                        "Prefer clear, actionable responses."
                    ),
                },
                {"role": "user", "content": prompt},
            ],
        }
        try:
            resp = requests.post(OPENROUTER_URL, headers=headers, json=data, timeout=60)
            if resp.status_code == 200:
                payload = resp.json()
                return payload.get("choices", [{}])[0].get("message", {}).get("content")
            elif resp.status_code in (401, 403):
                continue  # Try next model
            elif resp.status_code == 429:
                return "Rate limited. Try again later."
            else:
                print(f"Model {model} failed: {resp.status_code}")
        except Exception as exc:
            print(f"Model {model} error: {exc}")
            continue
    
    return "All AI models failed. Check your API key and internet connection."



def verify_api() -> Optional[str]:
    """Return None if OK, else a human-readable error string."""
    if not OPENROUTER_API_KEY:
        return "OPENROUTER_API_KEY is missing."
    
    # Try multiple free models
    models_to_try = [
        "meta-llama/llama-3.1-8b-instruct:free",
        "microsoft/phi-3-mini-128k-instruct:free", 
        "google/gemma-2-9b-it:free",
        "deepseek/deepseek-r1:free"
    ]
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "HTTP-Referer": HTTP_REFERER,
        "Referer": HTTP_REFERER,
        "X-Title": APP_TITLE,
    }
    
    for model in models_to_try:
        data = {
            "model": model,
            "messages": [{"role": "user", "content": "hi"}],
            "max_tokens": 5,
        }
        try:
            resp = requests.post(OPENROUTER_URL, headers=headers, json=data, timeout=15)
            if resp.status_code == 200:
                print(f"✓ Working model found: {model}")
                return None
            elif resp.status_code in (401, 403):
                print(f"✗ {model}: Auth failed")
                continue  # Try next model
            elif resp.status_code == 429:
                return "Rate limited (429). Try again later."
            else:
                print(f"✗ {model}: {resp.status_code} - {resp.text[:100]}")
        except Exception as exc:
            print(f"✗ {model}: {exc}")
            continue
    
    return "All free models failed. Your key may be invalid or restricted."

