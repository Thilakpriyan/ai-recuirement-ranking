import numpy as np

from src.models.embedding_model import EmbeddingModel
from src.utils import build_candidate_text


class CandidateRetriever:

    def __init__(self):

        print("Loading Embedding Model...")

        self.model = EmbeddingModel()

    def search(
            self,
            index,
            df,
            job_description,
            top_k=200
    ):

        print("Encoding Job Description...")

        query_embedding = self.model.encode(
            [job_description]
        )

        query_embedding = np.asarray(
            query_embedding,
            dtype=np.float32
        )

        print("Searching FAISS Index...")

        scores, indices = index.search(
            query_embedding,
            top_k
        )

        results = []

        for score, idx in zip(
                scores[0],
                indices[0]
        ):

            if idx == -1:
                continue

            candidate = df.iloc[idx].to_dict()

            results.append({

                "candidate_id":
                    candidate["candidate_id"],

                "semantic_score":
                    float(score),

                "row_index":
                    int(idx),

                "candidate_text":
                    build_candidate_text(candidate),

                "candidate_data":
                    candidate

            })

        print(f"Retrieved {len(results)} candidates")

        return results