import streamlit as st
from scraper import fetch_remoteok_jobs
from matcher import load_resume, score_job

st.set_page_config(page_title="AI DevOps Agent", layout="wide")

st.title("🌍 AI DevOps Remote Job Agent")

jobs = fetch_remoteok_jobs()
resume = load_resume()

st.write("🔍 Jobs Found:", len(jobs))

if len(jobs) == 0:
    st.error("No jobs found — scraper issue")
    st.stop()

for job in jobs:

    score = score_job(job["title"], resume)

    col1, col2 = st.columns([3, 1])

    with col1:
        st.subheader(job["title"])
        st.write("🏢", job["company"])
        st.write("📍", job["location"])
        st.write("📊 Match:", score)

    with col2:
        if job["link"]:
            st.link_button("🔗 Apply", job["link"])
        else:
            st.write("No link")

    st.markdown("---")