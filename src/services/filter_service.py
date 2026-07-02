from typing import Dict
import pandas as pd


class FilterService:

    @staticmethod
    def skill_overlap(candidate_skills, jd_skills):

        candidate = {
            s["name"].lower()
            for s in candidate_skills
        }

        jd = {
            s.lower()
            for s in jd_skills
        }

        return len(candidate & jd)

    @staticmethod
    def filter_candidates(df: pd.DataFrame, jd_features: Dict):

        filtered = df.copy()

        # Experience
        filtered = filtered[
            filtered["profile"].apply(
                lambda p:
                jd_features["min_experience"]
                <= p["years_of_experience"]
                <= jd_features["max_experience"] + 2
            )
        ]

        # Open to work
        filtered = filtered[
            filtered["redrob_signals"].apply(
                lambda s: s["open_to_work_flag"]
            )
        ]

        # Profile completeness
        filtered = filtered[
            filtered["redrob_signals"].apply(
                lambda s:
                s["profile_completeness_score"] >= 60
            )
        ]

        # GitHub activity
        filtered = filtered[
            filtered["redrob_signals"].apply(
                lambda s:
                s["github_activity_score"] >= 5
            )
        ]

        # At least one matching JD skill
        filtered = filtered[
            filtered["skills"].apply(
                lambda skills:
                FilterService.skill_overlap(
                    skills,
                    jd_features["skills"]
                ) >= 1
            )
        ]

        return filtered