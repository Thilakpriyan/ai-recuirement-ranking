from src.loader import DataLoader
from src.retrieval import CandidateRetriever

jd = DataLoader.load_job_description()

retriever = CandidateRetriever()

results = retriever.search(
    jd,
    top_k=5
)

for r in results:

    print("=" * 80)

    print("Candidate :", r["candidate_id"])

    print("Semantic Score :", round(r["semantic_score"], 4))

    print("Row :", r["row_index"])

    print()

    print(r["candidate_text"][:500])