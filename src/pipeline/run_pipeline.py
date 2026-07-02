import pandas as pd

from src.loader import DataLoader
from src.features.jd_features import JDFeatureExtractor
from src.services.filter_service import FilterService
from src.services.ranking_service import RankingService
from src.pipeline.build_index import CandidateIndexer
from src.retrieval import CandidateRetriever
from src.models.cross_encoder import CrossEncoderRanker
from src.utils import normalize, weighted_score
from src.config import OUTPUT_DIR


def main():

    print("=" * 60)
    print("AI Recruitment Ranking Pipeline")
    print("=" * 60)

    # -------------------------------------------------
    # Load Job Description
    # -------------------------------------------------

    print("\nLoading Job Description...")

    job_description = DataLoader.load_job_description()

    # -------------------------------------------------
    # Extract JD Features
    # -------------------------------------------------

    print("Extracting JD Features...")

    jd_features = JDFeatureExtractor.extract(
        job_description
    )

    # -------------------------------------------------
    # Load Candidate Dataset
    # -------------------------------------------------

    print("\nLoading Candidate Dataset...")

    df = DataLoader.load_candidates().head(10000)

    print(f"Loaded {len(df)} candidates")

    # -------------------------------------------------
    # Structured Filtering
    # -------------------------------------------------

    print("\nFiltering Candidates...")

    filtered_df = FilterService.filter_candidates(
        df,
        jd_features
    )

    print(
        f"Candidates after filtering : {len(filtered_df)}"
    )

    # -------------------------------------------------
    # Recruiter Ranking
    # -------------------------------------------------

    print("\nCalculating Recruiter Score...")

    ranked_df = RankingService.rank(
        filtered_df,
        jd_features
    )

    print(
        f"Candidates after recruiter ranking : {len(ranked_df)}"
    )

    # -------------------------------------------------
    # Build FAISS Index
    # -------------------------------------------------

    print("\nBuilding Semantic Index...")

    indexer = CandidateIndexer()

    index = indexer.build(ranked_df)
    # -------------------------------------------------
    # Semantic Retrieval
    # -------------------------------------------------

    print("\nRunning Semantic Retrieval...")

    retriever = CandidateRetriever()

    semantic_results = retriever.search(
        index=index,
        df=ranked_df,
        job_description=job_description,
        top_k=200
    )

    semantic_df = pd.DataFrame(semantic_results)

    print(
        f"Semantic candidates retrieved : {len(semantic_df)}"
    )

    # -------------------------------------------------
    # Cross Encoder Re-ranking
    # -------------------------------------------------

    print("\nRunning Cross Encoder...")

    cross_encoder = CrossEncoderRanker()

    candidate_texts = semantic_df[
        "candidate_text"
    ].tolist()

    cross_scores = cross_encoder.rerank(
        job_description,
        candidate_texts
    )

    semantic_df["cross_score"] = cross_scores

    # -------------------------------------------------
    # Merge Recruiter Score
    # -------------------------------------------------

    recruiter_scores = ranked_df[
        [
            "candidate_id",
            "recruiter_score"
        ]
    ]

    final_df = semantic_df.merge(
        recruiter_scores,
        on="candidate_id",
        how="left"
    )

    # -------------------------------------------------
    # Normalize Scores
    # -------------------------------------------------

    print("\nNormalizing Scores...")

    final_df["semantic_norm"] = normalize(
        final_df["semantic_score"]
    )

    final_df["cross_norm"] = normalize(
        final_df["cross_score"]
    )

    final_df["recruiter_norm"] = normalize(
        final_df["recruiter_score"]
    )

    # -------------------------------------------------
    # Final Weighted Score
    # -------------------------------------------------

    print("\nCalculating Final Score...")

    final_df["final_score"] = final_df.apply(
        lambda row: weighted_score(
            row["recruiter_norm"],
            row["semantic_norm"],
            row["cross_norm"]
        ),
        axis=1
    )

    final_df = final_df.sort_values(
        "final_score",
        ascending=False
    )
    # -------------------------------------------------
    # Display Top Candidates
    # -------------------------------------------------

    print("\n" + "=" * 70)
    print("TOP 20 RECOMMENDED CANDIDATES")
    print("=" * 70)

    print(
        final_df[
            [
                "candidate_id",
                "recruiter_score",
                "semantic_score",
                "cross_score",
                "final_score"
            ]
        ].head(20)
    )

    # -------------------------------------------------
    # Save Submission
    # -------------------------------------------------

    # -------------------------------------------------
    # Generate Submission
    # -------------------------------------------------

    print("\nGenerating Submission File...")

    submission = final_df.copy()

    # Rank
    submission["rank"] = range(1, len(submission) + 1)

    # Normalize final score to 0-1
    submission["score"] = normalize(
        submission["final_score"]
    )

    # Generate recruiter explanation
    reasoning = []

    for _, row in submission.iterrows():
        candidate = row["candidate_data"]

        profile = candidate["profile"]

        signals = candidate["redrob_signals"]

        skills = candidate["skills"]

        candidate_skill_names = {
            s["name"].lower()
            for s in skills
        }

        jd_skill_names = {
            s.lower()
            for s in jd_features["skills"]
        }

        ai_skill_count = len(
            candidate_skill_names &
            jd_skill_names
        )

        reason = (
            f"{profile['current_title']} with "
            f"{profile['years_of_experience']:.1f} yrs; "
            f"{ai_skill_count} AI/core skills; "
            f"response rate "
            f"{signals['recruiter_response_rate']:.2f}."
        )

        reasoning.append(reason)

    submission["reasoning"] = reasoning

    submission = submission[
        [
            "candidate_id",
            "rank",
            "score",
            "reasoning"
        ]
    ]

    OUTPUT_DIR.mkdir(
        exist_ok=True
    )

    submission.to_csv(
        OUTPUT_DIR / "submission.csv",
        index=False
    )

    print("\nSubmission Saved Successfully!")

    print(
        OUTPUT_DIR / "submission.csv"
    )

if __name__ == "__main__":
    main()