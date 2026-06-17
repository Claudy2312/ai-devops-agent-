def load_resume():
    with open("resume.txt", "r", encoding="utf-8") as f:
        return f.read().lower()


def score_job(job_title, resume):

    job_title = job_title.lower()
    resume = resume.lower()

    skills = resume.split(",")

    score = 0

    for skill in skills:
        if skill.strip() in job_title:
            score += 12

    # bonus scoring logic
    if "aws" in job_title:
        score += 15
    if "devops" in job_title:
        score += 10
    if "remote" in job_title:
        score += 10

    return min(score, 100)