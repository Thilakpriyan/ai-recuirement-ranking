import faiss
import numpy as np

from src.models.embedding_model import EmbeddingModel
from src.utils import build_candidate_text


class CandidateIndexer:

    def __init__(self):

        self.model = EmbeddingModel()

    def build(self, df):

        print(f"Building index for {len(df)} candidates...")

        texts = [
            build_candidate_text(row.to_dict())
            for _, row in df.iterrows()
        ]

        embeddings = self.model.encode(texts)

        embeddings = embeddings.astype(np.float32)

        index = faiss.IndexFlatIP(
            embeddings.shape[1]
        )

        index.add(embeddings)

        return index