import streamlit as st
import requests
import fitz  # PyMuPDF


# Function to extract text from PDF
def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text


# Set the title of the app
st.title("Document Summarization")

# Create a file uploader for document upload
uploaded_file = st.file_uploader("Choose a document", type=["txt", "pdf"])

# Text preview and submission button
if uploaded_file is not None:
    # Check the file type and extract text accordingly
    if uploaded_file.type == "application/pdf":
        content = extract_text_from_pdf(uploaded_file)
    else:
        content = uploaded_file.read().decode('utf-8')

    st.text_area("Document Preview", content, height=300, max_chars=10000)

    # Summarize button
    if st.button("Summarize"):
        # Make a POST request to the machine learning model
        url = "http://localhost:8501"  # Replace with your actual URL
        response = requests.post(url, json={"text": content})

        if response.status_code == 200:
            summary = response.json().get("summary")
            st.subheader("Summary:")
            st.write(summary)
        else:
            st.error("Error: Could not get a summary. Please try again.")
