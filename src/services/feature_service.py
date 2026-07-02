import pandas as pd

from src.utils import build_candidate_text


class FeatureService:

    @staticmethod
    def get_candidate_texts(df: pd.DataFrame):

        texts = []

        for _, row in df.iterrows():

            texts.append(
                build_candidate_text(
                    row.to_dict()
                )
            )

        return texts