from typing import Dict
import numpy as np


def normalize(values):
    values = np.array(values, dtype=float)

    min_v = values.min()
    max_v = values.max()

    if max_v == min_v:
        return np.ones_like(values)

    return (values - min_v) / (max_v - min_v)


def weighted_score(recruiter, semantic, cross):
    return (
        0.25 * recruiter +
        0.35 * semantic +
        0.40 * cross
    )


def build_candidate_text(candidate: Dict) -> str:
    """
    Converts a candidate JSON into a recruiter-friendly summary
    suitable for embedding.
    """

    profile = candidate["profile"]
    skills = candidate["skills"]
    history = candidate["career_history"]
    education = candidate["education"]
    signals = candidate["redrob_signals"]

    skill_text = ", ".join(
        s["name"] for s in skills
    )

    history_text = "\n".join(
        f"{job['title']} at {job['company']} ({job['duration_months']} months). {job['description']}"
        for job in history
    )

    education_text = "\n".join(
        f"{edu['degree']} in {edu['field_of_study']} from {edu['institution']}"
        for edu in education
    )

    return f"""
Candidate

Headline:
{profile['headline']}

Summary:
{profile['summary']}

Experience:
{profile['years_of_experience']} years

Current Company:
{profile['current_company']}

Career History:
{history_text}

Education:
{education_text}

Skills:
{skill_text}

Behavior:
Profile Score: {signals['profile_completeness_score']}

Github Activity: {signals['github_activity_score']}

Open To Work: {signals['open_to_work_flag']}
"""