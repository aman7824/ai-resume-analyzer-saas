from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_score(resume, job_desc):
    cv = CountVectorizer()
    matrix = cv.fit_transform([resume, job_desc])
    score = cosine_similarity(matrix)[0][1]
    return round(score * 100, 2)

def get_feedback(resume, job_desc):
    resume_words = set(resume.lower().split())
    job_words = set(job_desc.lower().split())

    missing = job_words - resume_words

    feedback = ""

    if missing:
        feedback += "❌ Missing Skills:\n"
        feedback += ", ".join(list(missing)[:15]) + "\n\n"
    else:
        feedback += "✅ No major missing keywords found\n\n"

    feedback += "💡 Suggestions:\n"
    feedback += "- Add more relevant skills from job description\n"
    feedback += "- Improve project descriptions\n"
    feedback += "- Use strong action words (Developed, Built, Designed)\n"
    feedback += "- Add measurable achievements\n"

    return feedback
