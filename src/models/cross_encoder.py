from sentence_transformers import CrossEncoder


class CrossEncoderRanker:

    def __init__(self):

        print("Loading Cross Encoder...")

        self.model = CrossEncoder(
            "cross-encoder/ms-marco-MiniLM-L-6-v2"
        )

    def rerank(
            self,
            job_description,
            candidate_texts
    ):

        pairs = [
            (job_description, text)
            for text in candidate_texts
        ]

        scores = self.model.predict(
            pairs
        )

        return scores