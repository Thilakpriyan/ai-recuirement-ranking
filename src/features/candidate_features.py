from typing import Dict, List


class CandidateFeatureExtractor:

    AI_SKILLS = {
        "Machine Learning",
        "Deep Learning",
        "LLM",
        "LLMs",
        "Fine-tuning LLMs",
        "NLP",
        "RAG",
        "Vector Database",
        "Milvus",
        "LangChain",
        "PyTorch",
        "TensorFlow",
        "Computer Vision",
        "Image Classification",
        "Speech Recognition",
        "LoRA",
        "GANs",
        "Transformers",
        "MLOps",
        "BentoML",
        "Weights & Biases",
    }

    CLOUD_SKILLS = {
        "AWS",
        "Azure",
        "GCP",
    }

    BACKEND_SKILLS = {
        "Python",
        "Flask",
        "FastAPI",
        "Django",
        "SQL",
        "Spark",
        "Kafka",
        "Airflow",
    }

    @staticmethod
    def extract(candidate: Dict):

        profile = candidate["profile"]

        skills = candidate["skills"]

        history = candidate["career_history"]

        signals = candidate["redrob_signals"]

        skill_names = {
            s["name"] for s in skills
        }

        ai_count = len(
            skill_names &
            CandidateFeatureExtractor.AI_SKILLS
        )

        cloud_count = len(
            skill_names &
            CandidateFeatureExtractor.CLOUD_SKILLS
        )

        backend_count = len(
            skill_names &
            CandidateFeatureExtractor.BACKEND_SKILLS
        )

        total_duration = sum(
            j["duration_months"]
            for j in history
        )

        avg_job_duration = (
            total_duration / len(history)
            if history else 0
        )

        return {

            "candidate_id":
                candidate["candidate_id"],

            "experience":
                profile["years_of_experience"],

            "ai_skill_count":
                ai_count,

            "cloud_skill_count":
                cloud_count,

            "backend_skill_count":
                backend_count,

            "profile_score":
                signals["profile_completeness_score"],

            "github_score":
                signals["github_activity_score"],

            "response_rate":
                signals["recruiter_response_rate"],

            "assessment_scores":
                signals["skill_assessment_scores"],

            "avg_job_duration":
                avg_job_duration,

            "open_to_work":
                signals["open_to_work_flag"],

            "relocation":
                signals["willing_to_relocate"],

            "current_company_size":
                profile["current_company_size"],

            "industry":
                profile["current_industry"]

        }