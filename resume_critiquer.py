"""
AI Resume Critiquer (free Gemini API version)

Setup:
1. pip install streamlit pypdf2 python-dotenv google-genai
2. Free API key lein: https://aistudio.google.com/apikey
3. Isi folder mein ".env" file banayein aur likhein:
       GEMINI_API_KEY=apni_key_yahan
4. Run karein:  streamlit run resume_critiquer.py
"""

import io
import os

import PyPDF2
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Agar model ka naam kaam na kare to yahan naya naam likh dein
MODEL_NAME = "gemini-2.5-flash"

st.set_page_config(page_title="AI Resume Critiquer", page_icon="📃", layout="centered")
st.title("AI Resume Critiquer")
st.markdown("Apna resume upload karein aur AI se feedback lein!")

uploaded_file = st.file_uploader("Resume upload karein (PDF ya TXT)", type=["pdf", "txt"])
job_role = st.text_input("Kis job role ke liye apply kar rahe hain? (optional)")
analyze = st.button("Analyze Resume")


def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += (page.extract_text() or "") + "\n"
    return text


def extract_text(file):
    if file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(file.read()))
    return file.read().decode("utf-8")


if analyze and uploaded_file:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        st.error("GEMINI_API_KEY nahi mili. .env file check karein.")
        st.stop()

    try:
        content = extract_text(uploaded_file)

        if not content.strip():
            st.error("File mein koi text nahi mila.")
            st.stop()

        role = job_role if job_role else "general job applications"
        prompt = f"""You are an expert resume reviewer with years of HR experience.
The candidate is a fresher. Analyze this resume and give constructive feedback on:
1. Content clarity and impact
2. Skills presentation
3. Projects and experience descriptions
4. Specific improvements for: {role}

Give a clear, structured answer with specific recommendations.

Resume:
{content}
"""

        client = genai.Client(api_key=api_key)
        with st.spinner("Analyzing..."):
            response = client.models.generate_content(model=MODEL_NAME, contents=prompt)

        st.markdown("### Analysis Results")
        st.markdown(response.text)

    except Exception as e:
        st.error(f"Error aaya: {e}")
