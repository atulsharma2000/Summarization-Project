import streamlit as st


home_page = st.page(
    page="views/home_page.py",
    title= "Home Page",
    icon=":material/account_circle:",
    default = True,
)

daily_news_page = st.Page(
    page= "views/daily_news.py",
    title= "Daily News", 
    icon = ":material/breaking_news:"  
)

sentiment_page = st.page(
    page="views/sentiment.py",
    title= "Sentiment Analysis",
    icon=":material/emoticon_satisfied:",
)

pg = st.navigation(
    {
        "home": [home_page],
        "news_page": [daily_news_page,sentiment_page]
    }
)

st.sidebar.text("Made by Atul 🧑‍💻 and Harsh 🧑‍💻")
pg.run()