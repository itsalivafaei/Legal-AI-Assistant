from .gradio_user_interface import pain_ui
from .speech_to_text import whis_init
from .large_language_model import generate_response


def process_input(text, audio):
    if audio is not None:
        question = whis_init(audio)
    elif text:
        question = text
    else:
        return 'Please provide text or audio input.', None

    print("================================ Question Transcribed ================================")
    print(question)
    print("================================ Question Transcribed ================================")

    response, audio_output = generate_response(question)

    print("================================ Response Generated ================================")
    print(response)
    print("================================ Response Generated ================================")

    return response, audio_output


def main():
    pain_ui(process_input)


if __name__ == "__main__":
    main()
