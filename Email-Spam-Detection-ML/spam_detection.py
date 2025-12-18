import pandas as pd
import nltk
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

from url_utils import extract_urls, is_suspicious_url
from image_utils import extract_text_from_image




nltk.download('stopwords')

# Load dataset
df = pd.read_csv("spam.csv", encoding="latin-1")
df = df[['v1', 'v2']]
df.columns = ['label', 'message']

# Clean text
def clean_text(text):
    text = text.lower()
    text = ''.join(c for c in text if c not in string.punctuation)
    words = text.split()
    words = [w for w in words if w not in stopwords.words('english')]
    return ' '.join(words)

df['clean_message'] = df['message'].apply(clean_text)

# Vectorize
vectorizer = TfidfVectorizer(max_features=3000)
X = vectorizer.fit_transform(df['clean_message'])
y = df['label'].map({'ham': 0, 'spam': 1})

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = MultinomialNB()
model.fit(X_train, y_train)

print("Model Accuracy:", accuracy_score(y_test, model.predict(X_test)))

# Predict function
def predict_spam(text):
    text = clean_text(text)
    vector = vectorizer.transform([text])
    return "Spam" if model.predict(vector)[0] == 1 else "Ham"

# Real-world detection
def real_world_spam_detector(text, image_path=None):
    score = 0

    if predict_spam(text) == "Spam":
        score += 1

    for url in extract_urls(text):
        if is_suspicious_url(url):
            score += 1

    if image_path:
        image_text = extract_text_from_image(image_path)
        if predict_spam(image_text) == "Spam":
            score += 1

    return "Spam" if score >= 2 else "Ham"


print(real_world_spam_detector(
    "Win cash now http://free-prize.com"
))
def real_world_spam_detector(text, image_path=None):
    score = 0

    # Text ML detection
    if predict_spam(text) == "Spam":
        score += 1

    # URL check
    for url in extract_urls(text):
        if is_suspicious_url(url):
            score += 1

    # Image OCR check
    if image_path:
        image_text = extract_text_from_image(image_path)
        if predict_spam(image_text) == "Spam":
            score += 1

    return "Spam" if score >= 2 else "Ham"



