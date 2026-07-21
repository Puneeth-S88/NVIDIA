"""
Day 7 - Interactive Chatbot
Loads the model trained by train_chatbot.py and lets you chat with
it directly in the terminal output. Run this AFTER train_chatbot.py.

Usage:
    python chatbot.py
    (type your message and press Enter; type 'quit' to exit)
"""
import json
import pickle
import random

import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer()

intents = json.load(open('intents.json', 'r', encoding='utf-8'))
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.h5')


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(w.lower()) for w in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words(sentence)
    prediction = model.predict(np.array([bow]), verbose=0)[0]

    ERROR_THRESHOLD = 0.25
    results = [[i, p] for i, p in enumerate(prediction) if p > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)

    if not results:
        return [{"intent": "unknown", "probability": "1.0"}]

    return [
        {"intent": classes[r[0]], "probability": str(r[1])}
        for r in results
    ]


def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    for intent in intents_json['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])
    return "I'm not sure how to respond to that."


def chat():
    print("=" * 60)
    print("  Day 7 Chatbot - type 'quit' to exit")
    print("=" * 60)

    while True:
        message = input("You: ")
        if message.lower() in ("quit", "exit", "bye"):
            print("Bot: Goodbye! Have a great day!")
            break

        intents_list = predict_class(message)
        response = get_response(intents_list, intents)
        print(f"Bot: {response}")


if __name__ == "__main__":
    chat()