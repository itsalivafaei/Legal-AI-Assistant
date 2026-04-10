import os
from gtts import gTTS

_DIR = os.path.dirname(os.path.abspath(__file__))
_STATIC_DIR = os.path.join(_DIR, "static")
os.makedirs(_STATIC_DIR, exist_ok=True)


def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    audio_file = os.path.join(_STATIC_DIR, "output.mp3")
    tts.save(audio_file)
    return audio_file
