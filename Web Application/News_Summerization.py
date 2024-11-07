import streamlit as st
import requests

import streamlit as st
from streamlit_google_auth import Authenticate

authenticator = Authenticate(
    secret_credentials_path='google_credentials.json',
    cookie_name='my_cookie_name',
    cookie_key='this_is_secret',
    redirect_uri='http://localhost:8501',
)

# Function to fetch news title
def fetch_news_title():
    # Sample URL for the Google News API (replace with an actual API endpoint)
    url = "https://newsapi.org/v2/everything?q=tesla&from=2024-10-07&sortBy=publishedAt&apiKey=c8334439bd36423c89cb3157b3365a6f"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Extract the title of the first news article
        title = data['articles'][0]['content']
        return title
    else:
        st.error("Failed to fetch news.")
        return None

# Function to determine sentiment (dummy logic for example purposes)
def get_sentiment(text):
    # Dummy sentiment logic: if the title contains 'good', it's positive; otherwise, negative
    if 'good' in text.lower():
        return 'good'
    else:
        return 'bad'

# Set the title of the app
st.markdown("<h1 style='text-align: center; color: white; background-color: #4CAF50; padding: 10px; border-radius: 5px;'>News Summarization</h1>", unsafe_allow_html=True)

# Apply CSS styles
st.markdown(""" <style> body { background-color: #f4f4f4; } .container { display: flex; justify-content: space-between; } .title-box { background-color: #848c8a; padding: 20px; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); width: 65%; margin: 20px; } .sentiment-circle-container { display: flex; justify-content: center; align-items: center; width: 30%; margin: 20px; } .sentiment-circle { width: 150px; height: 150px; border-radius: 50%; } .button-container { display: flex; justify-content: center; align-items: center; margin: 20px; } .login-button { background-color: green; color: white; border: none; padding: 10px 20px; text-align: center; text-decoration: none; font-size: 16px; cursor: pointer; border-radius: 10px; } .login-button:hover { background-color: darkgreen; } </style> """, unsafe_allow_html=True)
# Fetch news title
news_title = fetch_news_title()

# Display news title in a styled box
if news_title:
    st.markdown("""
    <div class="container">
        <div class="title-box">
            <h2>{}</h2>
        </div>
        <div class="sentiment-circle-container">
            <div class="sentiment-circle" style="background-color: {};"></div>
        </div>
    </div>
    """.format(news_title, 'green' if get_sentiment(news_title) == 'good' else 'red'), unsafe_allow_html=True)


st.markdown('<button class="login-button">Login For Better Recommendation</button>', unsafe_allow_html=True)

