import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

def train_model(csv_path="dataset\combined_emails_with_natural_pii.csv"):
    df = pd.read_csv(csv_path)
    X = df['email']
    y = df['type']

    model = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', MultinomialNB())
    ])
    model.fit(X, y)
    joblib.dump(model, 'model/classifier.pkl')

def predict_category(email_text):
    model = joblib.load('model/classifier.pkl')
    return model.predict([email_text])[0]
