import requests
from config import KEYWORDS

def fetch_remoteok_jobs():
    url = "https://remoteok.com/api"
    data = requests.get(url).json()

    jobs = []

    for job in data:
        title = str(job.get("position", "")).lower()

        if any(k in title for k in KEYWORDS):

            jobs.append({
                "title": job.get("position"),
                "company": job.get("company"),
                "link": job.get("url"),
                "location": job.get("location", ""),
                "type": "remoteok"
            })

    return jobs