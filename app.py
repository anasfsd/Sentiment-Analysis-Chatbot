# Install required libraries
# Uncomment and run the following lines on Google Colab
# !pip install transformers streamlit pyngrok -q

# Import necessary libraries
from transformers import pipeline
import streamlit as st

# Load the pre-trained sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

# Function to analyze sentiment
def analyze_sentiment(text):
    result = sentiment_analyzer(text)[0]
    label = result['label']
    if label == "POSITIVE":
        return "positive"
    elif label == "NEGATIVE":
        return "negative"
    else:
        return "neutral"

# Streamlit application interface
st.title("Sentiment Analysis Chatbot")
st.write("Enter a sentence, and I'll tell you if the sentiment is positive, negative, or neutral!")

# Input box for the user
user_input = st.text_input("Type your message here:")

# Display sentiment analysis result
if user_input:
    sentiment = analyze_sentiment(user_input)
    st.write(f"**Sentiment:** {sentiment}")

# To run this app locally in Google Colab, use the following code:
# from pyngrok import ngrok
# public_url = ngrok.connect(port="8501")
# print(f"Public URL: {public_url}")
# !streamlit run app.py --server.port=8501
