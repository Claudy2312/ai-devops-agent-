import requests
from config import KEYWORDS

def fetch_remoteok_jobs():
    url = "https://remoteok.com/api"
    headers = {"User-Agent": "Mozilla/5.0"}

    res = requests.get(url, headers=headers)
    data = res.json()

    jobs = []

    for job in data[1:]:  # skip metadata

        title = str(job.get("position", "")).lower()

        if any(k in title for k in KEYWORDS):

            jobs.append({
                "title": job.get("position", "No Title"),
                "company": job.get("company", "Unknown"),
                "link": job.get("url", ""),
                "location": job.get("location", "Worldwide"),
            })

    return jobs