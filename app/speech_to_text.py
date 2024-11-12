# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

import whisper

# Load the model once at startup
model = whisper.load_model("tiny")

# Initialize Whisper model
def whis_init(audio):
    print("================================ Whisper Model Loaded================================")

    result = model.transcribe(audio)
    print("================================ Whisper DONE================================")

    return result['text']
