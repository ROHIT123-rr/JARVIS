import speech_recognition as sr
from typing import Optional
from services.tts import TextToSpeech
from services.ai import chat as ai_chat, verify_api
from intents import parse_intent, dispatch
from config import WAKE_WORD, LISTEN_TIMEOUT, PHRASE_TIME_LIMIT, OPENROUTER_API_KEY


class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen(self, prompt: Optional[str] = None) -> Optional[str]:
        if prompt:
            print(prompt)
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio = self.recognizer.listen(
                    source,
                    timeout=LISTEN_TIMEOUT,
                    phrase_time_limit=PHRASE_TIME_LIMIT,
                )
            except Exception:
                return None
        try:
            text = self.recognizer.recognize_google(audio)
            print("Heard:", text)
            return text
        except Exception:
            return None

    def listen_for_wake_word(self) -> bool:
        heard = self.listen("🎤 Waiting for wake word…")
        if not heard:
            return False
        return WAKE_WORD in heard.lower()


def main():
    api_err = None
    if not OPENROUTER_API_KEY:
        api_err = "OpenRouter API key is missing. Set it in .env or env.example or via $env:OPENROUTER_API_KEY."
    else:
        api_err = verify_api()
    if api_err:
        print("Jarvis:", api_err)
        return
    stt = SpeechToText()
    tts = TextToSpeech()

    print("Jarvis:", "Hello, I am Jarvis. Say 'Jarvis' to activate me.")
    tts.speak("Hello, I am Jarvis. Say 'Jarvis' to activate me.")

    while True:
        if not stt.listen_for_wake_word():
            continue

        print("Jarvis:", "Yes? What would you like me to do?")
        tts.speak("Yes? What would you like me to do?")
        command = stt.listen("🎤 Listening for command…")
        if not command:
            tts.speak("I didn't catch that. Please repeat.")
            continue

        intent, arg = parse_intent(command)
        if intent == "exit":
            print("Jarvis:", "Goodbye! Have a great day.")
            tts.speak("Goodbye! Have a great day.")
            break

        handled = dispatch(intent, arg)
        if handled is not None:
            print("Jarvis:", handled)
            tts.speak(handled)
            if intent == "shutdown":
                break
            continue

        # Fallback to AI chat
        response = ai_chat(arg or command) or "Sorry, I couldn't get a response."
        print("Jarvis:", response)
        tts.speak(response)


if __name__ == "__main__":
    main()