from pathlib import Path
try:
    from dotenv import load_dotenv
    # Load env.example first (defaults), then .env to override
    base_dir = Path(__file__).parent
    example_path = base_dir / "env.example"
    if example_path.exists():
        load_dotenv(example_path, override=False)
    env_path = base_dir / ".env"
    if env_path.exists():
        load_dotenv(env_path, override=True)
except Exception:
    # dotenv is optional; environment variables still work without it
    pass
import os

# Environment / API
OPENROUTER_API_KEY = (os.getenv("OPENROUTER_API_KEY", "") or "").strip().strip('"')
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_MODEL = (os.getenv("OPENROUTER_MODEL", "meta-llama/llama-3.1-8b-instruct:free") or "meta-llama/llama-3.1-8b-instruct:free").strip().strip('"')

# Headers metadata (optional but recommended by OpenRouter)
HTTP_REFERER = os.getenv("HTTP_REFERER", "https://your-site-or-project.com")
APP_TITLE = os.getenv("APP_TITLE", "Jarvis Assistant")

# Speech settings
TTS_RATE = int(os.getenv("TTS_RATE", "150"))

# STT timeouts (seconds)
LISTEN_TIMEOUT = float(os.getenv("LISTEN_TIMEOUT", "6"))
PHRASE_TIME_LIMIT = float(os.getenv("PHRASE_TIME_LIMIT", "8"))

# Wake word
WAKE_WORD = os.getenv("WAKE_WORD", "jarvis")


