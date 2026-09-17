import streamlit as st
from PyPDF2 import PdfReader

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖"
)

st.title("🤖 AI Resume Analyzer")

st.write(
    "Upload your resume and compare it with a job description."
)

resume = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste the Job Description"
)
def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()or""
    return text    

if st.button("Analyze Resume"):
    if resume and job_description:
        resume_text = extract_text_from_pdf(resume)
        st.success("Resume uploaded and text extracted successfully!")
        st.subheader("Extracted Resume Text")
        st.write(resume_text)
    else:
        st.warning("Please upload your resume and enter a job description")    