import os
from groq import Groq
from transformers import pipeline
from dotenv import load_dotenv
load_dotenv()

# Initialize the Groq client
api_key = os.environ.get('GROQ_API_KEY')
client = Groq(api_key=api_key)

# Initialize the zero-shot classification pipline
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Test Groq connection
try:
    client.models.list()
    print("================================ Groq Connection Successful================================")
except Exception as e:
    print("================================ Groq Connection Failed================================")
    print("Error: ", e)

# Define Domain Restriction Logic
DOMAIN = 'legal issues'
DEFAULT_RESPONSE = 'This is out of my knowledge. Please try with related questions to legal issues.'


def is_relevant(question):
    candidate_labels = [DOMAIN, "other"]
    result = classifier(question, candidate_labels)

    # Check if DOMAIN has the highest score
    if result['labels'][0] == DOMAIN and result['scores'][0] > 0.7:
        return True
    else:
        return False
    # legal_keywords = ['law', 'legal', 'court', 'contract', 'rights']
    # return any(keyword in question.lower() for keyword in legal_keywords)


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
            return assistant_reply

        except Exception as e:
            print("================================ Groq Connection Failed================================")
            print("Error: ", e)
            return "I'm sorry, but I'm unable to provide a response at this time."

    else:
        return DEFAULT_RESPONSE
