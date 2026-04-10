
import os
import json
import base64

# Import existing logic
# from app.large_language_model import is_relevant
from speech_to_text import whis_init
# from text_to_speech import text_to_speech
from large_language_model import generate_response
# from gradio_user_interface import pain_ui


def main():
    # Read event data from environment variable (stringified JSON)
    event_data_str = os.environ.get('APPWRITE_CUNCTION_EVENT_DATA', '{}')
    event_data = json.loads(event_data_str)

    text = event_data.get('text', None)
    audio_base64 = event_data.get('audio', None)

    # TODO Ensure directories exist
    # NOTE: These directories are ephemeral within a single function run
    os.makedirs("static", exist_ok=True)
    os.makedirs("temp", exist_ok=True)

    question = None

    # Handle inputs
    if audio_base64:
        # Decode base64 audio data and save to a temp file
        audio_data = base64.b64decode(audio_base64)
        audio_path = "temp/input_audio.wav"
        with open(audio_path, "wb") as f:
            f.write(audio_data)
       
        # Transcribe the audio
        question = whis_init(audio_path)

        # Clean up
        os.remove(audio_path)

    elif text:
        question = text

    else:
        print(json.dumps({
            "error": "Please provide text or audio input."
        }))
        return
  
    # Generate response and possible an audio output
    response, audio_output_path = generate_response(question)

    # Prepare the result
    result = {
        "response": response,
        "audio_base64": None
    }

    if audio_output_path and os.path.exists(audio_output_path):
        # If there's an audio response, convert it to base64 to include in JSON response
        with open(audio_output_path, "rb") as f:
            audio_bytes = f.read()
        audio_out_base64 = base64.b64encode(audio_bytes).decode('utf-8')
        result["audio_base64"] = audio_out_base64

    # Print the result as JSON (this is the function output)
    print(json.dumps(result))


if __name__ == "__main__":
    main()







# ============================= FASTAPI FOR SERVER =============================


# from fastapi import FastAPI, File, UploadFile, Form
# from fastapi.responses import JSONResponse
# from fastapi.middleware.cors import CORSMiddleware
# from typing import Optional

# from mpmath.calculus.calculus import defun

# from app.large_language_model import is_relevant
# from speech_to_text import whis_init
# from text_to_speech import text_to_speech
# from large_language_model import generate_response
# from gradio_user_interface import pain_ui

# import os

# app = FastAPI()

# # Enable CORS (Cross-Origin Resource Sharing)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"]
# )

# # Ensure directories exist
# os.makedirs("static", exist_ok=True)
# os.makedirs("temp", exist_ok=True)

# @app.post("/process")
# async def process(
#         text: Optional[str] = Form(None),
#         audio: Optional[UploadFile] = Form(None)
# ):
#     if audio is None:
#         # Save the uploaded audio file
#         audio_path = f"temp/{audio.filename}"
#         with open(audio_path, "wb") as buffer:
#             buffer.write(await audio.read())

#         # Transcribe the audio
#         question = whis_init(audio_path)
#         os.remove(audio_path)
#     elif text:
#         question = text
#     else:
#         return JSONResponse(
#             status_code=400,
#             content={"error": "Please provide text or audio input."}
#         )

#     print("Question: ", question)

#     # based on is_relevant() return response and audio_output_path or default values
#     response, audio_output_path = generate_response(question)

#     # Prepare the response
#     result = {
#         "response": response,
#         "audio_url": None
#     }

#     if audio_output_path:
#         # In production, serve this file via a static files server
#         result["audio_url"] = f"/static/{os.path.basename(audio_output_path)}"

#     return JSONResponse(content=result)


# # Serve Static files
# from fastapi.staticfiles import StaticFiles
# app.mount("/static", StaticFiles(directory="static"), name="static")

# ============================= FASTAPI FOR SERVER =============================




# def process_input(text, audio):
#     if audio is not None:
#         audio_file
#  = audio  # Use the audio filepath directly
#         result = whis_init(audio_file)
#         question = result['text']
#     elif text:
#         question = text
#     else:
#         return 'Please provide text or audio input.', None
#
#     print("================================ Question Transcribed================================")
#     print(question)
#     print("================================ Question Transcribed================================")
#
#     response = generate_response(question)
#
#     print("================================ Response Generated================================")
#     print(response)
#     print("================================ Response Generated================================")
#
#     audio_output = text_to_speech(response)
#
#     return response, audio_output
#
#
# def main():
#     pain_ui(process_input)
#
#
# if __name__ == "__main__":
#     main()
