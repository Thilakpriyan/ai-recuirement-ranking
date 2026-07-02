
from src.loader import DataLoader
from src.models.cross_encoder import CrossEncoderRanker
from src.services.feature_service import FeatureService

df = DataLoader.load_candidates().head(10)

jd = DataLoader.load_job_description()

texts = FeatureService.get_candidate_texts(df)

model = CrossEncoderRanker()

scores = model.rerank(
    jd,
    texts
)

for i, s in enumerate(scores):

    print(
        df.iloc[i]["candidate_id"],
        round(float(s), 4)
    )