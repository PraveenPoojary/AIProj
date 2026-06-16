# import streamlit as st
#
# st.title("AI Agent Chatbox")
# st.write("This is my first Streamlit AI Chatbox.")
#
# options = st.selectbox("Select a option",["Praveen", ""],  key="option")
# if options:
#     st.text_input(" Ask Anything...", value =f"{options}", key="name")
# st.button("Submit")
#
# if options:
#     st.write(f"You asked: {options}")
#
#

import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
# QA Test Case Generator
st.title("AI Chatbot")

requirement = st.text_area(
    "Enter Requirement/User Story"
)
# Generate functional, negative and edge test cases for:
if st.button("Submit"):
    prompt = f"""
    Generate functional, negative and edge test cases for:
    {requirement}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    st.write(response.text)