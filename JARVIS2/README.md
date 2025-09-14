## Jarvis Personal Assistant (Windows)

### Quick Start (No AI Required)
```bash
pip install -r requirements.txt
python jarvis_no_ai.py
```

### Setup with AI
1. Install Python 3.10+
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Get a free OpenRouter API key:
   - Go to https://openrouter.ai/
   - Sign up for free account
   - Generate API key
4. Set environment variables (PowerShell):
```powershell
$env:OPENROUTER_API_KEY = "sk-or-..."
```

### Run Options

**Voice Control (No AI):**
```bash
python jarvis_no_ai.py
```

**Voice Control (With AI):**
```bash
python jarvis.py
```

### Commands
- "open chrome"
- "search for weather in London"
- "open folder Downloads"
- "screenshot"
- "lock pc"
- "restart"
- "shutdown"
- "what time is it"
- Or ask questions (AI mode only)

### Notes
- On Windows, PyAudio may require extra install steps. If pip fails, try:
  - `pip install pipwin` then `pipwin install pyaudio`
- Ensure your microphone works and is the default input device.
- If API key fails, use `jarvis_no_ai.py` for PC control only.

