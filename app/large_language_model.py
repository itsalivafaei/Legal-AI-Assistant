from text_to_speech import text_to_speech
from natural_language_understanding import DOMAIN, is_relevant

import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

# Initialize the Groq client
api_key = os.environ.get('GROQ_API_KEY')
client = Groq(api_key=api_key)

DEFAULT_RESPONSE = 'This is out of my knowledge. Please try with related questions to legal issues.'


def generate_response(question):
    system_prompt = {
        "role": "system",
        "content": f"You are an expert in {DOMAIN}. Provide concise answers with maximum 150 characters to questions "
                   f"related to {DOMAIN}."
    }
    chat_history = [system_prompt, {"role": "user", "content": question}]

    if is_relevant(question):
        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=chat_history,
                max_tokens=150,
                temperature=0.7
            )
            assistant_reply = response.choices[0].message.content
            audio_output_path = text_to_speech(assistant_reply)
            return assistant_reply, audio_output_path

        except Exception as e:
            print("================================ Groq Connection Failed================================")
            print("Error generating response: ", e)
            return "I'm sorry, but I'm unable to provide a response at this time.", None

    else:
        return DEFAULT_RESPONSE, None
