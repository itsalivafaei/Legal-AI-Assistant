import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import whisper


# Initialize Whisper model
def whis_init(audio):
    model = whisper.load_model("tiny", download_root="~/.cache/whisper")
    print("================================ Whisper Model Loaded================================")

    result = model.transcribe(audio)
    print("================================ Whisper DONE================================")

    return result
