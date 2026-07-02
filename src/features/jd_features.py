import re
from typing import Dict


class JDFeatureExtractor:

    AI_SKILLS = [
        "Python",
        "PyTorch",
        "TensorFlow",
        "LLM",
        "LLMs",
        "RAG",
        "LangChain",
        "Milvus",
        "Fine-tuning",
        "MLOps",
        "AWS",
        "Azure",
        "GCP",
        "Spark",
        "Kafka",
        "SQL",
        "Docker",
        "Kubernetes",
    ]

    @staticmethod
    def extract(jd_text: str) -> Dict:

        text = jd_text.lower()

        years = re.findall(r"(\d+)\s*[-–]\s*(\d+)\s*years", text)

        if years:
            min_exp = int(years[0][0])
            max_exp = int(years[0][1])
        else:
            min_exp = 0
            max_exp = 100

        found_skills = []

        for skill in JDFeatureExtractor.AI_SKILLS:

            if skill.lower() in text:
                found_skills.append(skill)

        return {

            "min_experience": min_exp,

            "max_experience": max_exp,

            "skills": found_skills,

            "remote": "remote" in text,

            "hybrid": "hybrid" in text,

            "relocation": "relocation" in text,

            "startup": "startup" in text,

            "leadership": (
                "lead" in text or
                "mentor" in text or
                "ownership" in text
            )

        }