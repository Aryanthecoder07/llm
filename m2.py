import streamlit as st
import requests

# Set up the Hugging Face API URL and headers
API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"
headers = {"Authorization": "Bearer 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"}

def summarize_text(input_text):
    # Prepare the payload for the API request
    payload = {"inputs": input_text}
    
    # Send the request to the Hugging Face API
    response = requests.post(API_URL, headers=headers, json=payload)
    
    # Extract and return the summary from the response
    if response.status_code == 200:
        return response.json()[0].get('summary_text', "No summary returned.")
    else:
        return f"Error: {response.status_code} - {response.text}"

# Streamlit app configuration
st.set_page_config(page_title="Text Summarizer", layout="centered", initial_sidebar_state="collapsed")
st.header("Text Summarizer")

# User input for the text to be summarized
input_text = st.text_area("Enter the text you want to summarize:", height=200)

# Button to trigger the summarization
if st.button("Summarize"):
    if input_text:
        summary = summarize_text(input_text)
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.error("Please enter some text to summarize.")
