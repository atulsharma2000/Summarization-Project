# import streamlit as st

# st.title("News Analysis")

# content = st.text_area("Enter News")
# submit_buton = st.form_submit_button("Submit")

# if submit_buton:
#     # Your code here to analyze the news content
#     # For example, you can use the Natural Language Toolkit (NLTK) library to perform sentiment


# ===============


import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Ensure you have the VADER lexicon downloaded
nltk.download("vader_lexicon")

# Initialize the sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

st.title("News Analysis")

# Create a form for user input
with st.form(key="news_form"):
    content = st.text_area("Enter News")
    submit_button = st.form_submit_button("Submit")

if submit_button:
    # Analyze the news content
    if content:
        # Get sentiment scores
        scores = analyzer.polarity_scores(content)

        # Display the results
        st.write("Sentiment Scores:")
        st.write(f"Positive: {scores['pos']:.2f}")
        st.write(f"Negative: {scores['neg']:.2f}")
        st.write(f"Neutral: {scores['neu']:.2f}")
        st.write(scores["compound"])
        # Determine overall sentiment
        if scores["compound"] >= 0.05:
            sentiment = "Positive"
            icon = ":material/mood:"
        elif scores["compound"] <= -0.05:
            sentiment = "Negative"
            icon = ":material/sentiment_dissatisfied:"
        else:
            sentiment = "Neutral"
            icon = ":material/sentiment_neutral:"

        st.write(f"Overall Sentiment: **{sentiment}**", icon)

    else:
        st.write("Please enter some news content to analyze.")
