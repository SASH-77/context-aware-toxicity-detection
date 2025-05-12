
# Install TextBlob library if you haven't already
# pip install textblob

from textblob import TextBlob

# A simple list of toxic words (you can expand this as needed)
toxic_words = ["hate", "worst", "stupid", "idiot", "angry", "dumb", "horrible", "terrible"]

# Function to detect sentiment using TextBlob
def detect_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"

# Function to check if the text contains toxic words
def detect_toxicity(text):
    # Check if any toxic word is in the text
    for word in toxic_words:
        if word.lower() in text.lower():
            return "Toxic"
    return "Non-toxic"

# Example texts for detection
texts = [
    "I hate how bad this is.",
    "You are such an idiot!",
    "I think this is great!",
    "This is the worst experience ever!"
]

# Run detection on sample texts
for text in texts:
    sentiment = detect_sentiment(text)
    toxicity = detect_toxicity(text)
    print(f"Text: {text}")
    print(f"Sentiment: {sentiment}")
    print(f"Toxicity: {toxicity}")
    print("-" * 50)
