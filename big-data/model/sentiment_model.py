import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load data
data = pd.read_csv("../data/twitter_clean.csv")

# Label otomatis
def label_sentiment(text):
    negative_words = ["lama", "antri", "kurang"]
    for w in negative_words:
        if w in text:
            return 0
    return 1

data["label"] = data["clean_text"].apply(label_sentiment)

# Vectorize
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data["clean_text"])
y = data["label"]

# Train model
model = MultinomialNB()
model.fit(X, y)

# Predict sentiment
data["predicted_sentiment"] = model.predict(X)
data["sentiment"] = data["predicted_sentiment"].map({
    1: "Positif",
    0: "Negatif"
})

# Save result
data.to_csv("../data/twitter_sentiment.csv", index=False)

print("File twitter_sentiment.csv berhasil dibuat")
