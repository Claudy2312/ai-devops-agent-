def load_resume():
    with open("resume.txt", "r", encoding="utf-8") as f:
        return f.read().lower()


def score_job(title, resume):

    title = title.lower()
    resume = resume.lower()

    skills = resume.split("\n")

    score = 0

    for skill in skills:
        if skill.strip() and skill.strip() in title:
            score += 10

    return min(score, 100)