import os
from gtts import gTTS

os.makedirs("static", exist_ok=True)


def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    audio_file = 'static/output.mp3'
    tts.save(audio_file)
    return audio_file
