import streamlit as st
from model import calculate_score, get_feedback
from utils import extract_text

st.title("📄 Resume Screening Tool (Free AI Version)")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
job_desc = st.text_area("Enter Job Description")

if uploaded_file and job_desc:
    resume_text = extract_text(uploaded_file)
    score = calculate_score(resume_text, job_desc)

    st.subheader(f"Match Score: {score}%")

    if score > 70:
        st.success("✅ Good Match")
    else:
        st.warning("❌ Improve Resume")

    if st.button("Get AI Feedback"):
        feedback = get_feedback(resume_text, job_desc)
        st.subheader("🤖 AI Suggestions")
        st.write(feedback)
