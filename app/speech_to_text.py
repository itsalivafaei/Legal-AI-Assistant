# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

import whisper

_model = None


def _get_model():
    global _model
    if _model is None:
        try:
            _model = whisper.load_model("tiny", download_root="~/.cache/whisper")
        except Exception as e:
            raise RuntimeError(f"Failed to load Whisper model: {e}") from e
    return _model


def whis_init(audio):
    model = _get_model()
    print("================================ Whisper Model Loaded================================")

    result = model.transcribe(audio)
    print("================================ Whisper DONE================================")

    return result['text']
