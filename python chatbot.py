import json
import random
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

nltk.download('punkt')
nltk.download('wordnet')

# Load and preprocess intents
lemmatizer = WordNetLemmatizer()
with open('intents.json') as file:
    data = json.load(file)

# Extract patterns and tags
corpus = []
tags = []
for intent in data['intents']:
    for pattern in intent['patterns']:
        tokens = nltk.word_tokenize(pattern)
        tokens = [lemmatizer.lemmatize(word.lower()) for word in tokens]
        sentence = " ".join(tokens)
        corpus.append(sentence)
        tags.append(intent['tag'])
# Vectorize patterns
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
y = tags

# Train a model
model = MultinomialNB()
model.fit(X, y)
def predict_intent(user_input):
    tokens = nltk.word_tokenize(user_input)
    tokens = [lemmatizer.lemmatize(word.lower()) for word in tokens]
    sentence = " ".join(tokens)
    X_test = vectorizer.transform([sentence])
    tag = model.predict(X_test)[0]
    return tag

def get_response(tag):
    for intent in data['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])

def chatbot():
    print("🤖 Chatbot: Hello! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit']:
            print("🤖 Chatbot: Goodbye!")
            break
        tag = predict_intent(user_input)
        response = get_response(tag)
        print(f"🤖 Chatbot: {response}")
if __name__ == "__main__":
    chatbot()
