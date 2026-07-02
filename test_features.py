from src.loader import DataLoader
from src.features.candidate_features import CandidateFeatureExtractor

df = DataLoader.load_candidates()

candidate = df.iloc[0].to_dict()

features = CandidateFeatureExtractor.extract(candidate)

for k, v in features.items():
    print(k, ":", v)