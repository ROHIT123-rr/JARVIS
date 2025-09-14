import pyttsx3
from config import TTS_RATE


class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", TTS_RATE)

    def speak(self, text: str) -> None:
        if not text:
            return
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception:
            # Avoid crashing if TTS engine throws
            pass

    def stop(self) -> None:
        try:
            self.engine.stop()
        except Exception:
            pass

    def set_rate(self, rate: int) -> None:
        try:
            self.engine.setProperty("rate", int(rate))
        except Exception:
            pass


