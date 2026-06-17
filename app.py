import streamlit as st
from scraper import fetch_remoteok_jobs
from matcher import load_resume, score_job

st.set_page_config(page_title="AI DevOps Job Agent", layout="wide")

st.title("🌍 AI DevOps Remote Job Agent")

resume = load_resume()
jobs = fetch_remoteok_jobs()

filtered_jobs = []

for job in jobs:
    score = score_job(job["title"], resume)

    if score >= 40:  # filter low quality jobs
        job["score"] = score
        filtered_jobs.append(job)

# sort by best match
filtered_jobs = sorted(filtered_jobs, key=lambda x: x["score"], reverse=True)

for job in filtered_jobs:

    st.subheader(job["title"])
    st.write("🏢 Company:", job["company"])
    st.write("📍 Location:", job["location"])
    st.write("📊 AI Match Score:", job["score"])

    st.link_button("🔗 Apply Now", job["link"])

    st.markdown("---")