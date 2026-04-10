from transformers import pipeline

# Initialize the zero-shot classification pipline
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Define Domain Restriction Logic
DOMAIN = 'legal issues'

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