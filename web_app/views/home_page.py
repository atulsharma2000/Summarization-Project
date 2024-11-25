import streamlit as st

st.title("New App")


# Sample data: List of news headlines and their URLs
news_data = [
    {"title": "Breaking News: Major Event Happens", "url": "https://example.com/news1"},
    {
        "title": "Sports Update: Team Wins Championship",
        "url": "https://example.com/news2",
    },
    {"title": "Technology: New Gadget Released", "url": "https://example.com/news3"},
]

# Displaying the news headings as clickable links
st.title("Latest News")
for news in news_data:
    st.markdown(f"[{news['title']}]({news['url']})")
