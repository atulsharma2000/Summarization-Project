import streamlit as st

# Define a function for each page
def home():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")

def page1():
    st.title("Page 1")
    st.write("Welcome to Page 1!")

def page2():
    st.title("Page 2")
    st.write("Welcome to Page 2!")

# Create a dictionary of pages
pages = {
    "Home": home,
    "Page 1": page1,
    "Page 2": page2
}

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", list(pages.keys()))

# Display the selected page
pages[page]()
