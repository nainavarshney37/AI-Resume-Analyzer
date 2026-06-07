import streamlit as st
from PyPDF2 import PdfReader

st.title("AI Resume Analyzer")

skills_db = [
    "python", "java", "c++", "html", "css",
    "javascript", "sql", "machine learning",
    "data science", "react"
]

uploaded_file = st.file_uploader("Upload Resume", type="pdf")

if uploaded_file:
    pdf = PdfReader(uploaded_file)

    text = ""
    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    text = text.lower()

    found_skills = [skill for skill in skills_db if skill in text]

    st.subheader("Skills Found")
    st.write(found_skills)

    score = (len(found_skills) / len(skills_db)) * 100

    st.subheader("Resume Score")
    st.progress(int(score))
    st.write(f"{score:.2f}%")

    missing = [skill for skill in skills_db if skill not in found_skills]

    st.subheader("Recommended Skills")
    st.write(missing)