from speech_to_text import whis_init
from text_to_speech import text_to_speech
from large_language_model import generate_response
from gradio_user_interface import pain_ui

import gradio as gr
from pydub import AudioSegment


def process_input(text, audio):
    if audio is not None:
        audio_file = audio  # Use the audio filepath directly
        result = whis_init(audio_file)
        question = result['text']
    elif text:
        question = text
    else:
        return 'Please provide text or audio input.', None

    print("================================ Question Transcribed================================")
    print(question)
    print("================================ Question Transcribed================================")

    response = generate_response(question)

    print("================================ Response Generated================================")
    print(response)
    print("================================ Response Generated================================")

    audio_output = text_to_speech(response)

    return response, audio_output


def main():
    pain_ui(process_input)


if __name__ == "__main__":
    main()
