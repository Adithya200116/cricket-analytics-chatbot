from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
import joblib

# Sample data (you should replace it with your actual training data)
questions = [
    "What is the total runs by player X?",
    "Who took the most wickets?",
    "Tell me the match details",
    "Who won the last match?",
    "How many balls did player Y face?"
]
categories = [
    "runs", "wickets", "match details", "match details", "balls"
]

# Create a model pipeline
model = make_pipeline(TfidfVectorizer(), LogisticRegression())

# Train the model
model.fit(questions, categories)

# Save the trained model
joblib.dump(model, "models/trained_model.pkl")
