import streamlit as st
from streamlit_navigation_bar import st_navbar

# Define the pages
pages = ["Home", "Summarization", "Text Summarization", "User Registration"]

# Optional: Define custom styles
styles = {
    "nav": {
        "background-color": "#7BD192",
    },
    "div": {
        "max-width": "32rem",
    },
    "span": {
        "border-radius": "0.5rem",
        "padding": "0.4375rem 0.625rem",
        "margin": "0 0.125rem",
    },
    "active": {
        "background-color": "rgba(255, 255, 255, 0.25)",
    },
}

# Define options for the navigation bar
options = {
    "show_menu": True,
    "show_sidebar": False,
    "fix_shadow": True,
    "use_padding": True,
}

# Create the navigation bar
st.set_page_config(initial_sidebar_state="collapsed")
page = st_navbar(pages, styles=styles, options=options)


# Define functions for each page
def home_page():
    st.write("Welcome to the Home Page")
    st.image("https://example.com/home-image.jpg", caption="Home Page Image")


def summarization_page():
    st.write("This is the Summarization Page")
    st.video("https://example.com/summarization-video.mp4")


def text_summarization_page():
    st.write("This is the Text Summarization Page")
    # Text areas for input and summary
    st.subheader("Text Summarization")
    text_input = st.text_area("Enter the text to be summarized", height=300)
    summary_button = st.button("Generate Summary")

    if summary_button and text_input:
        # Here you would call your deep learning model to generate the summary
        # For demonstration purposes, a simple summary function is used
        def generate_summary(text):
            # Replace this with your deep learning model's function
            return text[:100] + "..."

        summary = generate_summary(text_input)
        st.text_area("Summary", value=summary, height=100, disabled=True)


def user_registration_page():
    st.write("This is the User Registration Page")
    st.form("register_form")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    register_button = st.form_submit_button("Register")


# Navigate to the selected page
if page == "Home":
    home_page()
elif page == "Summarization":
    summarization_page()
elif page == "Text Summarization":
    text_summarization_page()
elif page == "User Registration":
    user_registration_page()

from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load your deep learning model and tokenizer
model = T5ForConditionalGeneration.from_pretrained('t5-small')
tokenizer = T5Tokenizer.from_pretrained('t5-small')


def generate_summary(text):
    input_text = "summarize: " + text
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    output = model.generate(input_ids)
    summary = tokenizer.decode(output, skip_special_tokens=True)
    return summary


def text_summarization_page():
    st.write("This is the Text Summarization Page")
    # Text areas for input and summary
    st.subheader("Text Summarization")
    text_input = st.text_area("Enter the text to be summarized", height=300)
    summary_button = st.button("Generate Summary")

    if summary_button and text_input:
        summary = generate_summary(text_input)
        st.text_area("Summary", value=summary, height=100, disabled=True)
