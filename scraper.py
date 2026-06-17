import requests
from config import KEYWORDS

def fetch_remoteok_jobs():
    url = "https://remoteok.com/api"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    jobs = []

    for job in data[1:]:  # IMPORTANT: skip first metadata row

        title = str(job.get("position", "")).lower()

        if any(k in title for k in KEYWORDS):

            jobs.append({
                "title": job.get("position"),
                "company": job.get("company"),
                "link": job.get("url"),
                "location": job.get("location", "Remote"),
            })

    return jobs