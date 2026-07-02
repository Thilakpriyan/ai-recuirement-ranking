import faiss
import numpy as np

from src.models.embedding_model import EmbeddingModel
from src.config import (
    FAISS_INDEX,
    ID_FILE
)


class CandidateRetriever:

    def __init__(self):

        print("Loading FAISS Index...")

        self.index = faiss.read_index(
            str(FAISS_INDEX)
        )

        self.ids = np.load(
            ID_FILE,
            allow_pickle=True
        )

        self.model = EmbeddingModel()

    def search(
            self,
            job_description,
            top_k=500
    ):

        query_embedding = self.model.encode(
            [job_description]
        )

        query_embedding = np.asarray(
            query_embedding,
            dtype="float32"
        )

        scores, indices = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for score, idx in zip(
                scores[0],
                indices[0]
        ):

            results.append({

                "candidate_id":
                    self.ids[idx],

                "semantic_score":
                    float(score)

            })

        return results