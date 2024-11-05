import streamlit as st
import requests
import pickle

entire_df = pickle.load(open('.pkl', "rb"))

content = entire_df['content']
summary = entire_df['Summary']

st.title("Text Summarization")

text_input = st.text_area("Enter text to summarize (max 1000 words):", max_chars=6000)

if st.button("Summarize"):
    if len(text_input.split()) > 1000:
        st.error("The input text exceeds 1000 words. Please shorten your text.")
    else:
        url = "https://example.com/api/summarize"

        response = requests.post(url, json={"text": text_input})

        if response.status_code == 200:
            summary = response.json().get("summary")
            st.subheader("Summary:")
            st.write(summary)
        else:
            st.error("Error: Could not get a summary. Please try again.")
