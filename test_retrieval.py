from src.loader import DataLoader
from src.retrieval import CandidateRetriever

jd = DataLoader.load_job_description()

retriever = CandidateRetriever()

results = retriever.search(
    jd,
    top_k=20
)

for r in results:

    print(r)