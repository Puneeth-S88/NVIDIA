"""
Day 7 - Chatbot Training Script
Trains a small neural network to classify user input into an
"intent" (greeting, goodbye, about_gpu, etc.) using a
bag-of-words representation. Same Keras skills as Day 5's CNN,
just applied to text instead of images.

Run this once to produce chatbot_model.h5, words.pkl, classes.pkl
Then run chatbot.py to actually chat.
"""
import json
import pickle
import random

import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

# ----------------------------------------------------------
# 1. Load dataset (intents.json)
# To use a real Kaggle dataset instead: download a chatbot/intents
# style dataset from Kaggle (e.g. search "chatbot intents dataset"),
# and reformat it into this same {"intents": [{"tag", "patterns",
# "responses"}]} structure, then point this script at that file.
# ----------------------------------------------------------
with open('intents.json', 'r', encoding='utf-8') as f:
    intents = json.load(f)

words = []
classes = []
documents = []
ignore_chars = ['?', '!', '.', ',']

# ----------------------------------------------------------
# 2. Tokenize every pattern sentence, build vocabulary
# ----------------------------------------------------------
for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_chars]
words = sorted(set(words))
classes = sorted(set(classes))

print(f"{len(documents)} training patterns")
print(f"{len(classes)} intent classes: {classes}")
print(f"{len(words)} unique lemmatized words")

# ----------------------------------------------------------
# 3. Build bag-of-words training data
# ----------------------------------------------------------
training = []
output_empty = [0] * len(classes)

for doc in documents:
    bag = []
    pattern_words = [lemmatizer.lemmatize(w.lower()) for w in doc[0]]
    for w in words:
        bag.append(1 if w in pattern_words else 0)

    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    training.append([bag, output_row])

random.shuffle(training)
train_x = np.array([row[0] for row in training])
train_y = np.array([row[1] for row in training])

# ----------------------------------------------------------
# 4. Build and train the neural network
# ----------------------------------------------------------
model = Sequential([
    Dense(128, input_shape=(len(train_x[0]),), activation='relu'),
    Dropout(0.5),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(len(train_y[0]), activation='softmax')
])

sgd = SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

model.fit(train_x, train_y, epochs=200, batch_size=8, verbose=1)

# ----------------------------------------------------------
# 5. Save the trained model + vocabulary for chatbot.py to use
# ----------------------------------------------------------
model.save('chatbot_model.h5')
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

print("\nTraining complete. Saved: chatbot_model.h5, words.pkl, classes.pkl")