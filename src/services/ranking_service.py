import pandas as pd


class RankingService:

    @staticmethod
    def recruiter_score(candidate, jd):

        profile = candidate["profile"]

        signals = candidate["redrob_signals"]

        skills = candidate["skills"]

        score = 0

        # Experience (25)

        exp = profile["years_of_experience"]

        if jd["min_experience"] <= exp <= jd["max_experience"]:
            score += 25
        elif exp > jd["max_experience"]:
            score += 18

        # Skills (25)

        candidate_skills = {
            s["name"].lower()
            for s in skills
        }

        jd_skills = {
            s.lower()
            for s in jd["skills"]
        }

        overlap = len(candidate_skills & jd_skills)

        score += overlap * 4

        # Github (10)

        score += min(
            signals["github_activity_score"],
            10
        )

        # Profile completeness (10)

        score += (
            signals["profile_completeness_score"] / 10
        )

        # Recruiter response (10)

        score += (
            signals["recruiter_response_rate"] * 10
        )

        # Assessments (20)

        assessment = signals[
            "skill_assessment_scores"
        ]

        if len(assessment):

            avg = (
                sum(
                    assessment.values()
                )
                /
                len(assessment)
            )

            score += avg / 5

        return round(score, 2)

    @staticmethod
    def rank(df, jd):

        scores = []

        for _, row in df.iterrows():

            candidate = row.to_dict()

            s = RankingService.recruiter_score(
                candidate,
                jd
            )

            scores.append(s)

        df = df.copy()

        df["recruiter_score"] = scores

        df = df.sort_values(
            "recruiter_score",
            ascending=False
        )

        return df.head(3000)