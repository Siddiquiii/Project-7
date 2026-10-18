# AI Resume Critiquer

A web app that reads your resume (PDF or TXT) and gives structured, AI-powered feedback using Google's Gemini API. You can also enter a target job role to get feedback tailored to it.

## Features
- Upload a resume as PDF or TXT
- Extracts text from the file automatically
- Optional job role input for tailored suggestions
- Feedback on content clarity, skills, projects and improvements

## Tech Stack
Python, Streamlit, PyPDF2, Google Gemini API

## How to Run
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Get a free API key from https://aistudio.google.com/apikey
3. Create a `.env` file in the project folder:
   ```
   GEMINI_API_KEY=your_key_here
   ```
4. Start the app:
   ```
   streamlit run resume_critiquer.py
   ```

## Live Demo
https://project-7-pftbyzrjytuggyw4efiryy.streamlit.app/

## Author
Muhammad Usman Siddiqui
