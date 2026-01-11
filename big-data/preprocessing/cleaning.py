import pandas as pd
import re

# Load twitter raw
twitter = pd.read_csv("../data/twitter_raw.csv")

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text

twitter["clean_text"] = twitter["tweet_text"].apply(clean_text)

twitter.to_csv("../data/twitter_clean.csv", index=False)
print("Twitter cleaned!")
