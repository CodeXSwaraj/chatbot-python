import spacy

# Load the spaCy model for NLP tasks
nlp = spacy.load("en_core_web_sm")

# Define intents and responses
intents = {
    "greeting": ["hello", "hi", "greetings", "what's up"],
    "goodbye": ["bye", "see you", "goodbye"],
    "thanks": ["thank you", "thanks"],
    "name": ["what is your name", "who are you"]
}

responses = {
    "greeting": "Hello! How can I assist you today?",
    "goodbye": "Goodbye! Have a great day!",
    "thanks": "You're welcome!",
    "name": "I'm a chatbot powered by spaCy and Tkinter!"
}

def classify_intent(user_input):
    doc = nlp(user_input.lower())
    for intent, keywords in intents.items():
        for keyword in keywords:
            if keyword in user_input:
                return intent
    return "unknown"

def get_response(intent):
    return responses.get(intent, "Sorry, I don't understand that.")
