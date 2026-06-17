import streamlit as st
from scraper import fetch_remoteok_jobs
from matcher import load_resume, score_job

st.title("🌍 AI DevOps Remote Job Agent")

jobs = fetch_remoteok_jobs()

st.write("🔍 DEBUG - Jobs found:", len(jobs))

resume = load_resume()

for job in jobs:

    score = score_job(job["title"], resume)

    if score < 30:
        continue

    st.subheader(job["title"])
    st.write(job["company"])
    st.write(job["location"])
    st.write("Match Score:", score)

    st.link_button("Apply", job["link"])